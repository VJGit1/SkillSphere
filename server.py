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
except ImportError as e:
    print(f"❌ Failed to import agent: {e}")
    root_agent = None

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
        "agent_loaded": root_agent is not None,
        "message": "SkillSphere backend is running"
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint for frontend communication"""
    if not root_agent:
        return jsonify({
            "error": "Agent not loaded",
            "message": "Please check agent.py file"
        }), 500
    
    try:
        data = request.json
        user_message = data.get('message', '')
        user_id = data.get('user_id', 'default_user')
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        # Call the agent with the user's message
        response = asyncio.run(call_agent_async(user_message, user_id))
        
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
    if not root_agent:
        return jsonify({"error": "Agent not loaded"}), 500
    
    try:
        data = request.json
        user_name = data.get('name', 'User')
        
        # Start the career journey
        response = asyncio.run(call_agent_async(
            f"Please start my career journey. My name is {user_name}",
            data.get('user_id', 'default_user')
        ))
        
        return jsonify({
            "status": "success",
            "response": response
        })
        
    except Exception as e:
        return jsonify({
            "error": "Failed to start journey",
            "message": str(e)
        }), 500

@app.route('/api/tools/<tool_name>', methods=['POST'])
def call_tool_directly(tool_name):
    """Direct tool calling endpoint for specific functionality"""
    if not root_agent:
        return jsonify({"error": "Agent not loaded"}), 500
    
    try:
        data = request.json
        
        # Map tool names to prompts
        tool_prompts = {
            'profile': f"Please collect my profile with this information: {json.dumps(data)}",
            'skills': f"Please analyze my resume: {data.get('resume_text', '')}",
            'careers': f"Please recommend careers based on my interests: {data.get('interests', '')}",
            'curriculum': f"Please create a learning plan for {data.get('career', '')}",
            'progress': f"Please track my progress: {data.get('completed_skills', '')}",
            'costs': f"Please calculate costs for {data.get('career', '')}",
            'scholarships': f"Please find scholarships for {data.get('career', '')}"
        }
        
        prompt = tool_prompts.get(tool_name, f"Please help me with {tool_name}")
        
        response = asyncio.run(call_agent_async(prompt, data.get('user_id', 'default_user')))
        
        return jsonify({
            "status": "success",
            "tool": tool_name,
            "response": response
        })
        
    except Exception as e:
        return jsonify({
            "error": f"Tool {tool_name} failed",
            "message": str(e)
        }), 500

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

async def call_agent_async(message: str, user_id: str = "default_user"):
    """Call the ADK agent asynchronously"""
    try:
        # In a real implementation, you would use the proper ADK session management
        # For now, we'll simulate an agent response
        
        # This is where you'd integrate with ADK's session management
        # session = await create_session(user_id)
        # response = await session.send_message(message)
        
        # For demo purposes, return a structured response
        return {
            "message": f"Agent response to: {message}",
            "user_id": user_id,
            "timestamp": "2025-10-03T12:00:00Z",
            "tools_used": [],
            "suggestions": [
                "Tell me about your background",
                "What career interests you?",
                "Would you like to analyze your skills?"
            ]
        }
        
    except Exception as e:
        raise Exception(f"Agent call failed: {str(e)}")

# =============================================================================
# STATIC FILE SERVING
# =============================================================================

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    return send_from_directory('static', filename)

if __name__ == '__main__':
    print("🚀 Starting SkillSphere Backend Server...")
    print(f"Agent Status: {'✅ Loaded' if root_agent else '❌ Not Loaded'}")
    print("📱 Frontend will be available at: http://localhost:5000")
    print("🔗 API endpoint: http://localhost:5000/api/chat")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )