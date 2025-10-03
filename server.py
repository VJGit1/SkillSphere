"""
SkillSphere Backend Server
Connects ADK agent to frontend applications
"""

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import asyncio
import json
import os
import sys

# Add the multi_tool_agent directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'multi_tool_agent'))

try:
    from agent import root_agent
    print("✅ Successfully imported SkillSphere agent")
    AGENT_AVAILABLE = True
except ImportError as e:
    print(f"❌ Failed to import agent: {e}")
    root_agent = None
    AGENT_AVAILABLE = False

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)  # Enable CORS for frontend connections

# =============================================================================
# API ENDPOINTS
# =============================================================================

@app.route('/')
def home():
    """Serve the main frontend page"""
    return render_template('index.html')

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "agent_loaded": AGENT_AVAILABLE,
        "message": "SkillSphere backend is running"
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint for frontend communication"""
    if not AGENT_AVAILABLE:
        return jsonify({
            "error": "Agent not loaded",
            "message": "Please check agent.py file and ADK installation"
        }), 500
    
    try:
        data = request.json
        user_message = data.get('message', '')
        user_id = data.get('user_id', 'default_user')
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        # Call the ADK agent directly
        response = call_agent_sync(user_message, user_id)
        
        return jsonify({
            "status": "success",
            "response": response,
            "user_id": user_id
        })
        
    except Exception as e:
        return jsonify({
            "error": "Agent execution failed",
            "message": str(e)
        }), 500

@app.route('/api/start-journey', methods=['POST'])
def start_journey():
    """Initialize a career guidance session"""
    if not AGENT_AVAILABLE:
        return jsonify({"error": "Agent not loaded"}), 500
    
    try:
        data = request.json
        user_name = data.get('name', 'User')
        
        # Start the career journey
        response = call_agent_sync(
            f"Please start my career journey. My name is {user_name}",
            data.get('user_id', 'default_user')
        )
        
        return jsonify({
            "status": "success",
            "response": response
        })
        
    except Exception as e:
        return jsonify({
            "error": "Failed to start journey",
            "message": str(e)
        }), 500

# =============================================================================
# AGENT INTEGRATION
# =============================================================================

def call_agent_sync(message: str, user_id: str = "default_user"):
    """
    Call the ADK agent synchronously using direct function calls.
    This is a simplified approach - in production you'd use ADK's session management.
    """
    try:
        # Import the tool functions from your agent
        from agent import (
            start_career_journey, manage_conversation_state, collect_user_profile,
            analyze_resume_skills, recommend_career_paths, generate_learning_curriculum,
            track_learning_progress, calculate_learning_costs, find_scholarships
        )
        
        # Simple keyword-based routing to demonstrate functionality
        message_lower = message.lower()
        
        if any(word in message_lower for word in ['hello', 'hi', 'start', 'begin', 'help']):
            # Extract name if mentioned
            import re
            name_match = re.search(r'my name is (\w+)', message_lower)
            name = name_match.group(1) if name_match else 'User'
            result = start_career_journey(name)
            return {
                "message": result.get("welcome_message", "Welcome to SkillSphere!"),
                "suggestions": result.get("next_steps", []),
                "type": "welcome"
            }
        
        elif any(word in message_lower for word in ['profile', 'about me', 'background']):
            # For demo, return profile collection guidance
            return {
                "message": "I'd love to learn about you! Please tell me:\n\n" +
                          "• Your name and current role\n" +
                          "• Years of experience\n" +
                          "• Your interests and passions\n" +
                          "• How you prefer to learn\n" +
                          "• How much time you can dedicate to learning daily",
                "suggestions": ["I'm a marketing graduate", "I have 2 years experience", "I'm interested in technology"],
                "type": "profile_collection"
            }
        
        elif any(word in message_lower for word in ['course', 'learn', 'curriculum', 'education']):
            # Extract career if mentioned
            career = "Software Developer"  # Default for demo
            if 'data' in message_lower:
                career = "Data Scientist"
            elif 'design' in message_lower or 'ux' in message_lower:
                career = "UX Designer"
            
            result = generate_learning_curriculum(career, "", "2-3 hours daily")
            curriculum = result.get("curriculum", {})
            
            response_message = f"🎓 **Learning Path for {career}**\n\n"
            response_message += f"**Duration:** {curriculum.get('duration', 'N/A')}\n\n"
            
            # Add top courses
            top_courses = curriculum.get('top_courses', [])
            if top_courses:
                response_message += "**🚀 Top 3 Recommended Courses:**\n"
                for i, course in enumerate(top_courses[:3], 1):
                    response_message += f"{i}. **{course['name']}** ({course['platform']})\n"
                    response_message += f"   Rating: {course['rating']} | Price: {course['price']}\n"
                    response_message += f"   🔗 {course['url']}\n\n"
            
            # Add certifications
            top_certs = curriculum.get('top_certifications', [])
            if top_certs:
                response_message += "**📜 Top 3 Certifications:**\n"
                for i, cert in enumerate(top_certs[:3], 1):
                    response_message += f"{i}. **{cert['name']}** ({cert['provider']})\n"
                    response_message += f"   Price: {cert['price']} | Duration: {cert['duration']}\n"
                    response_message += f"   🔗 {cert['url']}\n\n"
            
            return {
                "message": response_message,
                "suggestions": ["Calculate learning costs", "Find scholarships", "Track my progress"],
                "type": "curriculum"
            }
        
        elif any(word in message_lower for word in ['cost', 'price', 'money', 'budget', 'financial']):
            career = "Software Developer"  # Default for demo
            result = calculate_learning_costs(career, "online courses", "2-3 hours daily")
            
            cost_breakdown = result.get("cost_breakdown", {})
            time_costs = cost_breakdown.get("time_based_costs", {})
            
            response_message = f"💰 **Cost Analysis for {career}**\n\n"
            response_message += f"**Total Investment Range:**\n"
            response_message += f"• {cost_breakdown.get('total_range', {}).get('average', 'N/A')}\n\n"
            response_message += f"**Time-Based Breakdown:**\n"
            response_message += f"• Monthly: {time_costs.get('monthly_average', 'N/A')}\n"
            response_message += f"• Weekly: {time_costs.get('weekly_average', 'N/A')}\n"
            response_message += f"• Daily: {time_costs.get('daily_average', 'N/A')}\n\n"
            
            roi = result.get("roi_analysis", {})
            response_message += f"**ROI Analysis:**\n"
            response_message += f"• Potential Salary Increase: {roi.get('potential_salary_increase', 'N/A')}\n"
            response_message += f"• Break-even Time: {roi.get('break_even_time', 'N/A')}\n"
            
            return {
                "message": response_message,
                "suggestions": ["Find scholarships", "Explore payment plans", "Compare bootcamp costs"],
                "type": "financial"
            }
        
        elif any(word in message_lower for word in ['job', 'career', 'recommend', 'suggestion']):
            result = recommend_career_paths("technology, problem solving", "", "beginner")
            careers = result.get("recommended_careers", {})
            
            response_message = "🎯 **Career Recommendations Based on Your Interests:**\n\n"
            for career, details in list(careers.items())[:3]:
                response_message += f"**{career}**\n"
                response_message += f"• Salary: {details.get('avg_salary', 'N/A')}\n"
                response_message += f"• Growth: {details.get('job_growth', 'N/A')}\n"
                response_message += f"• Time to Proficiency: {details.get('time_to_proficiency', 'N/A')}\n\n"
            
            return {
                "message": response_message,
                "suggestions": ["Create learning plan", "Calculate costs", "Find job opportunities"],
                "type": "career_recommendations"
            }
        
        else:
            # Generic helpful response
            return {
                "message": "I'm SkillSphere, your AI career advisor! I can help you with:\n\n" +
                          "🎯 Career recommendations based on your interests\n" +
                          "📚 Personalized learning plans with real course links\n" +
                          "💰 Detailed cost analysis and financial planning\n" +
                          "📈 Progress tracking and motivation\n" +
                          "🎓 Scholarship and certification guidance\n\n" +
                          "What would you like to explore today?",
                "suggestions": [
                    "Help me choose a career",
                    "Show me learning resources", 
                    "Calculate learning costs",
                    "Find scholarships"
                ],
                "type": "general"
            }
            
    except Exception as e:
        print(f"Error calling agent: {e}")
        return {
            "message": f"I encountered an error: {str(e)}. Please try again.",
            "suggestions": ["Try a different question", "Check your connection"],
            "type": "error"
        }

# =============================================================================
# STATIC FILE SERVING
# =============================================================================

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    return send_from_directory('static', filename)

if __name__ == '__main__':
    print("🚀 Starting SkillSphere Backend Server...")
    print(f"Agent Status: {'✅ Loaded' if AGENT_AVAILABLE else '❌ Not Loaded'}")
    print("📱 Frontend will be available at: http://localhost:5000")
    print("🔗 API endpoint: http://localhost:5000/api/chat")
    print("\n💡 How this works:")
    print("1. Your .env file provides the Google API key")
    print("2. agent.py uses ADK + Gemini AI for intelligent responses")
    print("3. server.py calls your agent functions directly")
    print("4. Frontend (index.html) provides the beautiful UI")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )