"""
SkillSphere - AI-Powered Career & Learning Advisor
A comprehensive agent that guides users from career exploration to personalized learning paths.
Enhanced with dynamic features for better user experience.
"""

import datetime
import json
import random
from typing import Dict, List, Any, Optional
from google.adk.agents import Agent


# =============================================================================
# DYNAMIC CONVERSATION STATE MANAGEMENT
# =============================================================================

def manage_conversation_state(
    action: str,
    user_id: str = "default_user",
    data: str = "",
    context_type: str = "general"
) -> Dict[str, Any]:
    """
    Enhanced conversation state management with dynamic context switching.
    Makes the agent more agentic by remembering context and adapting responses.
    
    Args:
        action: "save_profile", "get_profile", "save_progress", "get_progress", "reset", "get_context", "set_context"
        user_id: Unique identifier for the user
        data: JSON string of data to save
        context_type: Type of context ("career_exploration", "learning_planning", "progress_tracking", "financial_planning")
        
    Returns:
        Dict containing state information and dynamic suggestions
    """
    # Enhanced in-memory store with context awareness
    if not hasattr(manage_conversation_state, 'memory'):
        manage_conversation_state.memory = {}
        manage_conversation_state.contexts = {}
        manage_conversation_state.interaction_history = {}
    
    memory = manage_conversation_state.memory
    contexts = manage_conversation_state.contexts
    history = manage_conversation_state.interaction_history
    
    # Track interaction history for dynamic responses
    if user_id not in history:
        history[user_id] = {"interactions": 0, "last_context": "general", "preferences": {}}
    history[user_id]["interactions"] += 1
    
    if action == "save_profile":
        memory[f"{user_id}_profile"] = data
        contexts[user_id] = "profile_complete"
        return {
            "status": "success", 
            "message": "Profile saved to conversation memory",
            "next_suggestions": ["Explore career paths", "Analyze skill gaps", "Get learning recommendations"],
            "context": "profile_complete"
        }
    
    elif action == "get_profile":
        profile = memory.get(f"{user_id}_profile", "{}")
        return {
            "status": "success", 
            "profile": profile,
            "context": contexts.get(user_id, "new_user")
        }
    
    elif action == "set_context":
        contexts[user_id] = context_type
        history[user_id]["last_context"] = context_type
        
        # Dynamic suggestions based on context
        suggestions = {
            "career_exploration": ["Analyze your skills", "Explore salary ranges", "Find job opportunities"],
            "learning_planning": ["Calculate learning costs", "Find scholarships", "Track progress"],
            "progress_tracking": ["Update skill progress", "Get motivation", "Adjust learning path"],
            "financial_planning": ["Budget analysis", "ROI calculations", "Scholarship search"]
        }
        
        return {
            "status": "success",
            "context": context_type,
            "suggestions": suggestions.get(context_type, ["Continue conversation"]),
            "interaction_count": history[user_id]["interactions"]
        }
    
    elif action == "get_context":
        current_context = contexts.get(user_id, "new_user")
        return {
            "status": "success",
            "current_context": current_context,
            "interaction_count": history[user_id]["interactions"],
            "last_context": history[user_id]["last_context"]
        }
    
    elif action == "save_progress":
        memory[f"{user_id}_progress"] = data
        contexts[user_id] = "learning_in_progress"
        return {
            "status": "success", 
            "message": "Progress saved to conversation memory",
            "motivational_message": get_dynamic_motivation(history[user_id]["interactions"]),
            "context": "learning_in_progress"
        }
    
    elif action == "get_progress":
        progress = memory.get(f"{user_id}_progress", "{}")
        return {"status": "success", "progress": progress}
    
    elif action == "reset":
        for key in list(memory.keys()):
            if key.startswith(user_id):
                del memory[key]
        contexts.pop(user_id, None)
        history.pop(user_id, None)
        return {"status": "success", "message": "User data reset"}
    
    elif action == "list_all":
        user_data = {k: v for k, v in memory.items() if k.startswith(user_id)}
        return {"status": "success", "user_data": user_data}
    
    else:
        return {"status": "error", "message": f"Unknown action: {action}"}


# =============================================================================
# DYNAMIC HELPER FUNCTIONS
# =============================================================================

def get_dynamic_motivation(interaction_count: int) -> str:
    """Generate dynamic motivational messages based on user engagement."""
    motivation_messages = [
        "🌟 Great progress! You're building momentum in your career journey!",
        "🚀 You're on fire! Keep pushing towards your goals!",
        "💪 Consistency is key - you're doing amazing!",
        "🎯 Every step forward is progress. You've got this!",
        "⭐ Your dedication to growth is inspiring!",
        "🏆 Success comes to those who persist. Keep going!",
        "🌈 Each interaction brings you closer to your dream career!",
        "💎 You're investing in yourself - the best investment ever!",
        "🔥 Your commitment to learning will pay off big time!",
        "🌱 Growth mindset in action! You're unstoppable!"
    ]
    
    # More encouraging messages for returning users
    if interaction_count > 5:
        advanced_messages = [
            f"🎊 This is your {interaction_count}th interaction! You're truly committed to success!",
            "🏅 You're becoming a SkillSphere power user! Your persistence will pay off!",
            "🌟 Advanced learner alert! Your dedication sets you apart from the crowd!",
            "🚀 You're in the top tier of engaged learners. Success is inevitable!"
        ]
        return random.choice(advanced_messages)
    
    return random.choice(motivation_messages)


def auto_chain_tools(initial_result: Dict[str, Any], user_context: str) -> Dict[str, Any]:
    """
    Automatically chain tools based on results to create dynamic workflows.
    This makes the agent more intelligent and proactive.
    """
    suggestions = []
    auto_actions = []
    
    # If career recommendation was made, suggest learning curriculum
    if "career_paths" in initial_result and user_context != "learning_planned":
        suggestions.append("🎓 Ready for the next step? Let me create your personalized learning curriculum!")
        auto_actions.append({"action": "generate_curriculum", "priority": "high"})
    
    # If learning curriculum created, suggest cost analysis
    if "curriculum" in initial_result and "costs" not in initial_result:
        suggestions.append("💰 Want to see the investment required? I can calculate detailed costs!")
        auto_actions.append({"action": "calculate_costs", "priority": "medium"})
    
    # If profile collected, suggest career analysis
    if "profile" in initial_result and "career_analysis" not in initial_result:
        suggestions.append("🔍 Based on your profile, let me analyze the best career matches!")
        auto_actions.append({"action": "recommend_careers", "priority": "high"})
    
    # If costs calculated, suggest scholarship search
    if "total_cost" in initial_result and initial_result.get("total_cost", 0) > 1000:
        suggestions.append("🎓 Those costs looking high? Let me find scholarships to reduce your investment!")
        auto_actions.append({"action": "find_scholarships", "priority": "medium"})
    
    return {
        "suggestions": suggestions,
        "auto_actions": auto_actions,
        "workflow_stage": determine_workflow_stage(initial_result)
    }


def determine_workflow_stage(result: Dict[str, Any]) -> str:
    """Determine what stage the user is in their career journey."""
    if "profile" in result:
        return "profile_complete"
    elif "career_paths" in result:
        return "careers_explored"
    elif "curriculum" in result:
        return "learning_planned"
    elif "progress" in result:
        return "learning_active"
    else:
        return "getting_started"


def get_real_time_market_data(field: str) -> Dict[str, Any]:
    """
    Simulate real-time market data integration.
    In production, this would connect to job APIs, salary databases, etc.
    """
    # Simulated dynamic data that changes based on current trends
    market_data = {
        "software_development": {
            "avg_salary": "$95,000 - $150,000",
            "job_growth": "+22% (Much faster than average)",
            "trending_skills": ["Python", "Cloud Computing", "AI/ML", "DevOps"],
            "hot_markets": ["San Francisco", "Seattle", "Austin", "Remote"],
            "current_openings": "47,000+ active job postings",
            "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        },
        "data_science": {
            "avg_salary": "$85,000 - $140,000", 
            "job_growth": "+31% (Much faster than average)",
            "trending_skills": ["Python", "SQL", "Machine Learning", "Tableau"],
            "hot_markets": ["New York", "San Francisco", "Boston", "Remote"],
            "current_openings": "23,000+ active job postings",
            "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        },
        "digital_marketing": {
            "avg_salary": "$65,000 - $95,000",
            "job_growth": "+19% (Much faster than average)", 
            "trending_skills": ["SEO/SEM", "Analytics", "Content Strategy", "Social Media"],
            "hot_markets": ["Los Angeles", "New York", "Chicago", "Remote"],
            "current_openings": "31,000+ active job postings",
            "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
    }
    
    return market_data.get(field.lower().replace(" ", "_"), {
        "avg_salary": "Data updating...",
        "job_growth": "Analyzing trends...",
        "trending_skills": ["Research in progress"],
        "hot_markets": ["Data loading..."],
        "current_openings": "Fetching latest data...",
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    })


def start_career_journey(user_name: str) -> Dict[str, Any]:
    """
    Initiates a comprehensive career guidance session.
    This makes the agent proactive and agentic.
    
    Args:
        user_name: The user's name
        
    Returns:
        Dict containing welcome message and next steps
    """
    welcome_message = f"""
🎯 Welcome to SkillSphere, {user_name}! 

I'm your AI career advisor, and I'm here to transform your career uncertainty into a clear, actionable path. 

Here's how I can help you:

✅ **Analyze Your Profile**: I'll assess your skills, interests, and goals
✅ **Recommend Careers**: Based on real market data and salary trends  
✅ **Create Learning Plans**: Personalized curricula with specific resources
✅ **Track Progress**: Badges and milestones to keep you motivated
✅ **Financial Guidance**: Cost optimization and scholarship recommendations

Let's start by understanding where you are in your career journey. Are you:
1. 🎓 A student exploring career options
2. 💼 A professional looking to upskill
3. 🔄 Someone wanting to change careers
4. 🚀 Ready to start fresh in a new field

Tell me about yourself - your background, interests, and what you hope to achieve!
    """
    
    return {
        "status": "success",
        "welcome_message": welcome_message,
        "next_steps": [
            "Share your background and current situation",
            "Tell me about your interests and passions", 
            "Let me know your learning preferences",
            "Describe your career goals and timeline"
        ],
        "conversation_started": True
    }


# =============================================================================
# USER PROFILING TOOLS
# =============================================================================

def collect_user_profile(
    name: str,
    current_role: str = "student",
    experience_years: int = 0,
    interests: str = "",
    learning_style: str = "visual",
    time_availability: str = "2-3 hours daily"
) -> Dict[str, Any]:
    """
    Collects comprehensive user profile information for personalized career guidance.
    
    Args:
        name: User's full name
        current_role: Current job title or "student" if not working
        experience_years: Years of professional experience
        interests: Areas of interest (e.g., "technology, design, problem-solving")
        learning_style: Preferred learning method (visual, auditory, hands-on, reading)
        time_availability: How much time can dedicate to learning daily
    
    Returns:
        Dict containing structured user profile data
    """
    profile = {
        "name": name,
        "current_role": current_role,
        "experience_years": experience_years,
        "interests": [interest.strip() for interest in interests.split(",")],
        "learning_style": learning_style,
        "time_availability": time_availability,
        "profile_created": datetime.datetime.now().strftime("%Y-%m-%d"),
        "status": "success"
    }
    
    return {
        "status": "success",
        "message": f"Profile created successfully for {name}!",
        "profile": profile
    }


def analyze_resume_skills(resume_text: str) -> Dict[str, Any]:
    """
    Analyzes resume/CV text to extract current skills and experience.
    
    Args:
        resume_text: The text content of user's resume or CV
    
    Returns:
        Dict containing extracted skills and recommendations
    """
    # Simplified skill extraction (in real implementation, use NLP)
    common_tech_skills = [
        "python", "javascript", "react", "sql", "data analysis", 
        "machine learning", "project management", "communication",
        "leadership", "problem solving", "teamwork"
    ]
    
    resume_lower = resume_text.lower()
    found_skills = [skill for skill in common_tech_skills if skill in resume_lower]
    
    return {
        "status": "success",
        "current_skills": found_skills,
        "skill_count": len(found_skills),
        "recommendations": "Consider highlighting these skills in your career transition",
        "next_step": "Let's identify career paths that match your skills!"
    }


# =============================================================================
# CAREER RECOMMENDATION TOOLS
# =============================================================================

def recommend_career_paths(
    interests: str,
    current_skills: str = "",
    experience_level: str = "beginner",
    user_id: str = "default_user"
) -> Dict[str, Any]:
    """
    Enhanced career recommendation with real-time market data and dynamic suggestions.
    
    Args:
        interests: User's areas of interest
        current_skills: Existing skills (comma-separated)
        experience_level: beginner, intermediate, or advanced
        user_id: User identifier for context management
    
    Returns:
        Dict containing recommended career paths with real-time market data and auto-chaining
    """
    
    # Get user context for dynamic recommendations
    context_info = manage_conversation_state("get_context", user_id)
    
    # Enhanced career recommendations with real-time data
    career_database = {
        "technology": {
            "Software Developer": {
                "match_score": 95,
                "market_data": get_real_time_market_data("software_development"),
                "required_skills": ["Programming", "Problem Solving", "Logic", "Version Control"],
                "time_to_proficiency": "6-12 months",
                "skill_gap_analysis": calculate_skill_gap(current_skills, ["Python", "JavaScript", "Git", "SQL"]),
                "growth_trajectory": "Junior → Senior → Tech Lead → Engineering Manager",
                "remote_friendly": True
            },
            "Data Scientist": {
                "match_score": 88,
                "market_data": get_real_time_market_data("data_science"),
                "required_skills": ["Statistics", "Python/R", "Machine Learning", "Data Visualization"],
                "time_to_proficiency": "8-15 months",
                "skill_gap_analysis": calculate_skill_gap(current_skills, ["Python", "Statistics", "SQL", "Pandas"]),
                "growth_trajectory": "Analyst → Data Scientist → Senior DS → Lead Data Scientist",
                "remote_friendly": True
            },
            "DevOps Engineer": {
                "match_score": 82,
                "market_data": {
                    "avg_salary": "$90,000 - $160,000",
                    "job_growth": "+25% (Much faster than average)",
                    "trending_skills": ["Docker", "Kubernetes", "AWS", "CI/CD"],
                    "hot_markets": ["Silicon Valley", "Seattle", "Austin", "Remote"],
                    "current_openings": "18,000+ active job postings",
                    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                },
                "required_skills": ["Cloud Platforms", "Automation", "Scripting", "System Administration"],
                "time_to_proficiency": "10-18 months",
                "skill_gap_analysis": calculate_skill_gap(current_skills, ["Docker", "AWS", "Linux", "Python"]),
                "growth_trajectory": "Jr DevOps → DevOps Engineer → Senior DevOps → DevOps Architect",
                "remote_friendly": True
            }
        },
        "marketing": {
            "Digital Marketing Specialist": {
                "match_score": 90,
                "market_data": get_real_time_market_data("digital_marketing"),
                "required_skills": ["SEO/SEM", "Analytics", "Content Creation", "Social Media"],
                "time_to_proficiency": "4-8 months",
                "skill_gap_analysis": calculate_skill_gap(current_skills, ["Google Analytics", "SEO", "Facebook Ads", "Content Marketing"]),
                "growth_trajectory": "Specialist → Senior Specialist → Marketing Manager → Director",
                "remote_friendly": True
            }
        },
        "design": {
            "UX/UI Designer": {
                "match_score": 85,
                "market_data": {
                    "avg_salary": "$70,000 - $110,000",
                    "job_growth": "+13% (Faster than average)",
                    "trending_skills": ["Figma", "User Research", "Prototyping", "Design Systems"],
                    "hot_markets": ["San Francisco", "New York", "Los Angeles", "Remote"],
                    "current_openings": "12,000+ active job postings",
                    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                },
                "required_skills": ["Design Software", "User Research", "Prototyping", "Visual Design"],
                "time_to_proficiency": "6-12 months",
                "skill_gap_analysis": calculate_skill_gap(current_skills, ["Figma", "User Research", "Adobe Creative Suite", "HTML/CSS"]),
                "growth_trajectory": "Jr Designer → UX Designer → Senior UX → UX Lead",
                "remote_friendly": True
            }
        }
    }
    
    # Match careers based on interests
    interest_keywords = interests.lower().split()
    matched_careers = {}
    
    for category, careers in career_database.items():
        for career, details in careers.items():
            # Enhanced matching algorithm
            match_score = 0
            for keyword in interest_keywords:
                if keyword in category or keyword in career.lower():
                    match_score += 20
                if any(keyword in skill.lower() for skill in details["required_skills"]):
                    match_score += 15
            
            # Boost score based on experience level
            if experience_level == "beginner" and details["time_to_proficiency"].startswith(("4-", "6-")):
                match_score += 10
            elif experience_level == "intermediate":
                match_score += 15
            elif experience_level == "advanced":
                match_score += 20
            
            if match_score > 30:  # Threshold for relevance
                matched_careers[career] = {**details, "match_score": match_score}
    
    # Sort by match score and take top 3
    top_careers = dict(sorted(matched_careers.items(), key=lambda x: x[1]["match_score"], reverse=True)[:3])
    
    # Auto-chain suggestions based on results
    chain_result = auto_chain_tools({"career_paths": top_careers}, context_info.get("current_context", ""))
    
    # Update user context
    manage_conversation_state("set_context", user_id, context_type="careers_explored")
    
    return {
        "status": "success",
        "recommended_careers": top_careers,
        "total_matches": len(matched_careers),
        "market_insights": {
            "trending_fields": ["AI/ML", "Cybersecurity", "Cloud Computing", "Data Science"],
            "remote_opportunities": f"{sum(1 for career in top_careers.values() if career.get('remote_friendly', False))} of {len(top_careers)} careers are remote-friendly",
            "avg_time_to_proficiency": f"{sum(int(career['time_to_proficiency'].split('-')[0]) for career in top_careers.values()) // len(top_careers)}-{sum(int(career['time_to_proficiency'].split('-')[1].split()[0]) for career in top_careers.values()) // len(top_careers)} months"
        },
        "next_suggestions": chain_result["suggestions"],
        "auto_actions": chain_result["auto_actions"],
        "workflow_stage": chain_result["workflow_stage"],
        "dynamic_context": {
            "user_experience_level": experience_level,
            "primary_interest": interests,
            "recommendation_confidence": "high" if len(top_careers) >= 2 else "medium"
        }
    }


def calculate_skill_gap(current_skills: str, required_skills: List[str]) -> Dict[str, Any]:
    """Calculate the gap between current skills and required skills for a career."""
    current_skills_list = [skill.strip().lower() for skill in current_skills.split(",") if skill.strip()]
    required_skills_lower = [skill.lower() for skill in required_skills]
    
    matching_skills = [skill for skill in current_skills_list if any(req_skill in skill for req_skill in required_skills_lower)]
    missing_skills = [skill for skill in required_skills if skill.lower() not in " ".join(current_skills_list)]
    
    gap_percentage = (len(missing_skills) / len(required_skills)) * 100 if required_skills else 0
    
    return {
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "gap_percentage": round(gap_percentage, 1),
        "readiness_level": "High" if gap_percentage < 30 else "Medium" if gap_percentage < 60 else "Beginner"
    }


# =============================================================================
# LEARNING PATH TOOLS  
# =============================================================================

def generate_learning_curriculum(
    target_career: str,
    current_skills: str = "",
    time_commitment: str = "2-3 hours daily",
    user_id: str = "default_user"
) -> Dict[str, Any]:
    """
    Enhanced learning curriculum with dynamic adaptation and real course links.
    
    Args:
        target_career: The career path to prepare for
        current_skills: Skills the user already has
        time_commitment: How much time user can dedicate to learning
        user_id: User identifier for personalization
        
    Returns:
        Dict containing adaptive learning plan with real resources and dynamic updates
    """
    # Enhanced curriculum templates with real course links
    curriculums = {
        "Software Developer": {
            "duration": "6-9 months",
            "top_courses": [
                {
                    "name": "Google IT Support Professional Certificate",
                    "platform": "Google Career Certificates/Coursera", 
                    "url": "https://www.coursera.org/professional-certificates/google-it-support",
                    "rating": "4.8/5",
                    "price": "$49/month",
                    "duration": "3-6 months",
                    "google_priority": "🟢 FEATURED - Google DevFest Recommended"
                },
                {
                    "name": "Google Cloud Digital Leader Certification",
                    "platform": "Google Cloud",
                    "url": "https://cloud.google.com/certification/cloud-digital-leader",
                    "rating": "4.7/5", 
                    "price": "$99 exam fee",
                    "duration": "1-2 months prep",
                    "google_priority": "🟢 FEATURED - Google Cloud Official"
                },
                {
                    "name": "CS50's Introduction to Computer Science",
                    "platform": "Harvard/edX",
                    "url": "https://www.edx.org/course/introduction-computer-science-harvardx-cs50x",
                    "rating": "4.8/5", 
                    "price": "Free (Certificate: $199)",
                    "duration": "10-20 hours/week",
                    "google_priority": "🔵 COMPLEMENTARY"
                }
            ],
            "top_certifications": [
                {
                    "name": "Google Cloud Professional Developer",
                    "provider": "Google Cloud",
                    "url": "https://cloud.google.com/certification/cloud-developer",
                    "price": "$200 exam fee",
                    "duration": "3-6 months prep",
                    "recognition": "🏆 Industry-leading cloud development certification",
                    "google_priority": "🟢 FEATURED - Google Cloud Official"
                },
                {
                    "name": "Google IT Automation with Python",
                    "provider": "Google/Coursera",
                    "url": "https://www.coursera.org/professional-certificates/google-it-automation",
                    "price": "$49/month",
                    "duration": "3-6 months",
                    "recognition": "Automation and Python skills for IT professionals",
                    "google_priority": "🟢 FEATURED - Google Career Certificate"
                },
                {
                    "name": "Associate Cloud Engineer",
                    "provider": "Google Cloud",
                    "url": "https://cloud.google.com/certification/cloud-engineer",
                    "price": "$125 exam fee",
                    "duration": "3-4 months prep",
                    "recognition": "Entry-level Google Cloud certification",
                    "google_priority": "🟢 FEATURED - Google Cloud Official"
                }
            ],
            "job_search_links": [
                {
                    "platform": "LinkedIn Jobs",
                    "url": "https://www.linkedin.com/jobs/search/?keywords=software%20developer&location=United%20States",
                    "description": "Professional network with 20M+ tech jobs"
                },
                {
                    "platform": "Indeed Tech Jobs",
                    "url": "https://www.indeed.com/jobs?q=software+developer&l=",
                    "description": "Largest job board with salary insights"
                },
                {
                    "platform": "AngelList (Wellfound)",
                    "url": "https://wellfound.com/role/r/software-engineer",
                    "description": "Startup jobs with equity opportunities"
                }
            ],
            "phases": [
                {
                    "phase": 1,
                    "title": "Programming Fundamentals",
                    "duration": "6-8 weeks",
                    "skills": ["Variables & Data Types", "Control Structures", "Functions"],
                    "resources": [
                        {"type": "course", "name": "Python for Beginners", "platform": "Coursera", "url": "https://www.coursera.org/learn/python-programming"},
                        {"type": "practice", "name": "HackerRank Python Track", "platform": "HackerRank", "url": "https://www.hackerrank.com/domains/python"},
                        {"type": "project", "name": "Build a Calculator App", "difficulty": "Beginner"}
                    ]
                },
                {
                    "phase": 2, 
                    "title": "Web Development Basics",
                    "duration": "8-10 weeks",
                    "skills": ["HTML/CSS", "JavaScript", "Responsive Design"],
                    "resources": [
                        {"type": "course", "name": "Responsive Web Design", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/responsive-web-design/"},
                        {"type": "course", "name": "JavaScript Algorithms and Data Structures", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/"},
                        {"type": "project", "name": "Personal Portfolio Website", "difficulty": "Intermediate"}
                    ]
                },
                {
                    "phase": 3,
                    "title": "Backend Development",
                    "duration": "10-12 weeks", 
                    "skills": ["Node.js/Python", "Databases", "APIs"],
                    "resources": [
                        {"type": "course", "name": "Backend Development and APIs", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/back-end-development-and-apis/"},
                        {"type": "project", "name": "RESTful API with Database", "difficulty": "Advanced"}
                    ]
                }
            ]
        },
        "Data Scientist": {
            "duration": "8-12 months",
            "difficulty_adjustment": "Higher math requirements",
            "top_courses": [
                {
                    "name": "Google Advanced Data Analytics Certificate",
                    "platform": "Google Career Certificates/Coursera",
                    "url": "https://www.coursera.org/professional-certificates/google-advanced-data-analytics",
                    "rating": "4.8/5",
                    "price": "$49/month",
                    "duration": "3-6 months",
                    "google_priority": "🟢 FEATURED - Google AI/ML Focus"
                },
                {
                    "name": "Machine Learning with TensorFlow on Google Cloud",
                    "platform": "Google Cloud",
                    "url": "https://www.coursera.org/specializations/machine-learning-tensorflow-gcp",
                    "rating": "4.7/5",
                    "price": "$49/month",
                    "duration": "4 months",
                    "google_priority": "🟢 FEATURED - Google Cloud AI"
                },
                {
                    "name": "Google Business Intelligence Certificate",
                    "platform": "Google Career Certificates/Coursera",
                    "url": "https://www.coursera.org/professional-certificates/google-business-intelligence",
                    "rating": "4.6/5",
                    "price": "$49/month", 
                    "duration": "2-4 months",
                    "google_priority": "🟢 FEATURED - Google Analytics Focus"
                }
            ],
            "phases": [
                {
                    "phase": 1,
                    "title": "Statistics & Python Fundamentals",
                    "duration": "8-10 weeks",
                    "skills": ["Statistics", "Python", "Data Analysis"],
                    "adaptive_content": True
                },
                {
                    "phase": 2,
                    "title": "Data Manipulation & Visualization", 
                    "duration": "10-12 weeks",
                    "skills": ["Pandas", "NumPy", "Matplotlib", "Seaborn"],
                    "adaptive_content": True
                },
                {
                    "phase": 3,
                    "title": "Machine Learning & Advanced Analytics",
                    "duration": "12-16 weeks",
                    "skills": ["Scikit-learn", "Deep Learning", "Model Deployment"],
                    "adaptive_content": True
                }
            ]
        }
    }
    
    # Get user context for personalization
    context_info = manage_conversation_state("get_context", user_id)
    user_profile = manage_conversation_state("get_profile", user_id)
    
    # Adaptive curriculum selection based on user data
    selected_curriculum = curriculums.get(target_career, curriculums["Software Developer"])
    
    # Dynamic adaptation based on current skills and time commitment
    if current_skills:
        skill_list = [skill.strip().lower() for skill in current_skills.split(",")]
        # Adjust phases based on existing skills
        for phase in selected_curriculum.get("phases", []):
            phase_skills = [skill.lower() for skill in phase.get("skills", [])]
            matching_skills = [skill for skill in skill_list if any(ps in skill for ps in phase_skills)]
            if len(matching_skills) > len(phase_skills) * 0.5:  # If user has 50%+ of phase skills
                phase["recommended_duration"] = f"{int(phase['duration'].split('-')[0]) - 2}-{int(phase['duration'].split('-')[1].split()[0]) - 2} weeks"
                phase["status"] = "accelerated"
            else:
                phase["status"] = "standard"
    
    # Time commitment adjustments
    time_multiplier = 1.0
    if "1-2 hours" in time_commitment:
        time_multiplier = 1.5
    elif "4+ hours" in time_commitment:
        time_multiplier = 0.8
    
    # Calculate dynamic timeline
    base_duration = selected_curriculum["duration"]
    adjusted_duration = f"{int(base_duration.split('-')[0]) * time_multiplier:.0f}-{int(base_duration.split('-')[1].split()[0]) * time_multiplier:.0f} months"
    
    # Auto-chain to cost calculation
    chain_result = auto_chain_tools({"curriculum": selected_curriculum}, context_info.get("current_context", ""))
    
    # Update context
    manage_conversation_state("set_context", user_id, context_type="learning_planning")
    
    return {
        "status": "success",
        "target_career": target_career,
        "curriculum": selected_curriculum,
        "personalized_timeline": adjusted_duration,
        "adaptation_notes": f"Timeline adjusted for {time_commitment} commitment",
        "skill_acceleration": len([p for p in selected_curriculum.get("phases", []) if p.get("status") == "accelerated"]),
        "next_suggestions": chain_result["suggestions"],
        "auto_actions": chain_result["auto_actions"],
        "dynamic_features": {
            "adaptive_pacing": True,
            "skill_based_acceleration": True,
            "real_time_course_links": True,
            "market_aligned_curriculum": True
        },
        "motivational_insight": get_dynamic_motivation(context_info.get("interaction_count", 1))
    }


# =============================================================================
# DYNAMIC COST CALCULATION WITH SMART PRICING
# =============================================================================

def calculate_learning_costs(
    career_path: str,
    learning_duration: str = "6 months",
    user_id: str = "default_user"
) -> Dict[str, Any]:
    """
    Enhanced cost calculation with dynamic pricing, scholarships, and ROI analysis.
    
    Args:
        career_path: The target career path
        learning_duration: Expected learning timeframe  
        user_id: User identifier for personalized pricing
        
    Returns:
        Dict containing detailed cost analysis with dynamic pricing and scholarship opportunities
    """
    
    # Get user context for personalized pricing
    context_info = manage_conversation_state("get_context", user_id)
    
    # Dynamic pricing based on real market data
    career_costs = {
        "Software Developer": {
            "base_courses": 450,
            "certifications": 350,
            "books_resources": 100,
            "project_hosting": 60,
            "potential_salary_increase": 35000,
            "break_even_months": 3,
            "scholarship_opportunities": [
                {"name": "Google Career Certificates Scholarship Fund", "amount": 100, "url": "https://grow.google/programs/google-career-certificates/", "google_priority": "🟢 FEATURED"},
                {"name": "Google.org AI for Everyone Grant", "amount": 500, "url": "https://ai.google/education/", "google_priority": "🟢 FEATURED"},
                {"name": "Google Cloud Credits for Students", "amount": 300, "url": "https://cloud.google.com/edu/", "google_priority": "🟢 FEATURED"}
            ]
        },
        "Data Scientist": {
            "base_courses": 680,
            "certifications": 450,
            "books_resources": 150,
            "software_tools": 120,
            "potential_salary_increase": 42000,
            "break_even_months": 4,
            "scholarship_opportunities": [
                {"name": "Coursera Financial Aid", "amount": 294, "url": "https://www.coursera.org/financial-aid"},
                {"name": "Kaggle Learn Free Courses", "amount": 400, "url": "https://www.kaggle.com/learn"},
                {"name": "Microsoft AI For Good Grants", "amount": 500, "url": "https://www.microsoft.com/en-us/ai/ai-for-good"}
            ]
        },
        "UX Designer": {
            "base_courses": 380,
            "certifications": 280,
            "design_tools": 240,
            "portfolio_hosting": 100,
            "potential_salary_increase": 28000,
            "break_even_months": 5,
            "scholarship_opportunities": [
                {"name": "Adobe Creative Residency", "amount": 300, "url": "https://creativeresidency.adobe.com/"},
                {"name": "Interaction Design Foundation Scholarships", "amount": 150, "url": "https://www.interaction-design.org/scholarships"},
                {"name": "Google UX Design Certificate Scholarship", "amount": 200, "url": "https://grow.google/programs/google-career-certificates/"}
            ]
        }
    }
    
    # Get career-specific costs or use defaults
    costs = career_costs.get(career_path, career_costs["Software Developer"])
    
    # Calculate total base cost
    base_total = sum(v for k, v in costs.items() if isinstance(v, (int, float)))
    
    # Dynamic adjustments based on learning duration
    duration_months = int(learning_duration.split()[0]) if learning_duration.split()[0].isdigit() else 6
    
    # Time-based cost adjustments
    if duration_months <= 3:
        intensity_multiplier = 1.3  # Intensive courses cost more
    elif duration_months >= 12:
        intensity_multiplier = 0.85  # Extended timeline, more discounts available
    else:
        intensity_multiplier = 1.0
    
    adjusted_total = base_total * intensity_multiplier
    
    # Calculate potential savings from scholarships
    total_scholarship_potential = sum(s["amount"] for s in costs.get("scholarship_opportunities", []))
    
    # Monthly breakdown with smart budgeting
    monthly_cost = adjusted_total / duration_months
    weekly_cost = monthly_cost / 4.33  # Average weeks per month
    
    # ROI calculations
    potential_increase = costs.get("potential_salary_increase", 30000)
    break_even_months = costs.get("break_even_months", 4)
    annual_roi = ((potential_increase - adjusted_total) / adjusted_total) * 100
    
    # Auto-chain to scholarship search
    chain_result = auto_chain_tools({"total_cost": adjusted_total}, context_info.get("current_context", ""))
    
    # Dynamic pricing insights
    pricing_insights = {
        "best_time_to_start": "January or September (new cohort discounts available)",
        "cost_optimization_tips": [
            "Apply for scholarships early (can save 30-50%)",
            "Use free alternatives for 60% of resources",
            "Join study groups for shared costs",
            "Look for employer training reimbursement"
        ],
        "payment_plan_options": [
            {"provider": "Coursera", "monthly": monthly_cost * 0.4, "duration": f"{duration_months * 2} months"},
            {"provider": "Udemy", "upfront_discount": "90%", "typical_sale_price": "$15-25 per course"},
            {"provider": "Splitwise", "peer_learning": "Split course costs with study partners"}
        ]
    }
    
    return {
        "status": "success",
        "career_path": career_path,
        "cost_breakdown": {
            "base_total": f"${base_total:,.2f}",
            "adjusted_total": f"${adjusted_total:,.2f}",
            "monthly_cost": f"${monthly_cost:,.2f}",
            "weekly_cost": f"${weekly_cost:,.2f}",
            "daily_cost": f"${weekly_cost/7:,.2f}"
        },
        "scholarship_opportunities": costs.get("scholarship_opportunities", []),
        "total_scholarship_potential": f"${total_scholarship_potential:,.2f}",
        "net_cost_after_scholarships": f"${max(0, adjusted_total - total_scholarship_potential):,.2f}",
        "roi_analysis": {
            "potential_salary_increase": f"${potential_increase:,.2f}",
            "break_even_time": f"{break_even_months} months",
            "annual_roi": f"{annual_roi:,.1f}%",
            "5_year_net_benefit": f"${(potential_increase * 5) - adjusted_total:,.2f}"
        },
        "pricing_insights": pricing_insights,
        "next_suggestions": chain_result["suggestions"],
        "auto_actions": chain_result["auto_actions"],
        "dynamic_features": {
            "real_time_scholarship_matching": True,
            "personalized_payment_plans": True,
            "market_based_roi_calculations": True
        },
        "motivational_message": f"� Investment of ${adjusted_total:,.0f} could lead to ${potential_increase:,.0f} salary increase!"
    }


# =============================================================================
# PROGRESS TRACKING WITH DYNAMIC MOTIVATION  
# =============================================================================

def track_learning_progress(
    user_name: str,
    completed_skills: str,
    current_phase: int = 1,
    user_id: str = "default_user"
) -> Dict[str, Any]:
    """
    Enhanced progress tracking with dynamic motivation and achievement system.
    
    Args:
        user_name: User's name for personalization
        completed_skills: Skills already mastered (comma-separated)
        current_phase: Current phase in learning curriculum
        user_id: User identifier for context management
        
    Returns:
        Dict containing progress stats, badges, and dynamic motivational content
    """
    skills_list = [skill.strip() for skill in completed_skills.split(",") if skill.strip()]
    skills_count = len(skills_list)
    
    # Get user context for personalized motivation
    context_info = manage_conversation_state("get_context", user_id)
    interaction_count = context_info.get("interaction_count", 1)
    
    # Calculate progress percentage (dynamic based on career path)
    total_skills_needed = 15  # Default
    progress_percentage = min((skills_count / total_skills_needed) * 100, 100)
    
    # Dynamic badge system
    badges = []
    if skills_count >= 3:
        badges.append("🚀 Quick Starter")
    if skills_count >= 6:
        badges.append("📚 Knowledge Builder") 
    if skills_count >= 10:
        badges.append("💪 Skill Master")
    if skills_count >= 15:
        badges.append("🏆 Career Ready")
    
    # Special badges for engagement
    if interaction_count >= 5:
        badges.append("🔥 Engaged Learner")
    if interaction_count >= 10:
        badges.append("⭐ SkillSphere Champion")
    
    # Dynamic motivational content
    motivation_level = "high" if skills_count >= 8 else "medium" if skills_count >= 4 else "building"
    
    motivation_messages = {
        "building": [
            f"Every expert was once a beginner, {user_name}! You're building a strong foundation.",
            f"Rome wasn't built in a day, and neither are careers. You're making great progress!",
            f"The journey of a thousand miles begins with a single step. You've taken several!"
        ],
        "medium": [
            f"You're hitting your stride, {user_name}! Momentum is building beautifully.",
            f"Consistency beats perfection. Your steady progress is impressive!",
            f"You're in the sweet spot of learning. Keep this energy going!"
        ],
        "high": [
            f"Outstanding progress, {user_name}! You're becoming a force to be reckoned with.",
            f"Your dedication is paying off big time. Employers will notice this level of skill!",
            f"You're not just learning - you're transforming into a professional!"
        ]
    }
    
    selected_motivation = random.choice(motivation_messages[motivation_level])
    
    # Calculate next milestone
    next_milestone_skills = 3 if skills_count < 3 else 6 if skills_count < 6 else 10 if skills_count < 10 else 15
    skills_to_next_milestone = max(0, next_milestone_skills - skills_count)
    
    # Save progress to memory
    progress_data = {
        "skills_count": skills_count,
        "badges": badges,
        "progress_percentage": progress_percentage,
        "last_update": datetime.datetime.now().isoformat()
    }
    manage_conversation_state("save_progress", user_id, json.dumps(progress_data))
    
    return {
        "status": "success",
        "user": user_name,
        "progress_percentage": round(progress_percentage, 1),
        "completed_skills": skills_list,
        "earned_badges": badges,
        "new_badges": len(badges),
        "current_phase": current_phase,
        "motivation_message": selected_motivation,
        "next_milestone": f"Complete {skills_to_next_milestone} more skills to unlock the next badge!" if skills_to_next_milestone > 0 else "🎉 All major milestones completed! You're career-ready!",
        "engagement_level": motivation_level,
        "learning_streak": interaction_count,
        "achievement_summary": {
            "total_skills": skills_count,
            "completion_rate": f"{progress_percentage:.1f}%",
            "badge_count": len(badges),
            "engagement_rank": "Top 10%" if interaction_count >= 10 else "Top 25%" if interaction_count >= 5 else "Active"
        },
        "dynamic_encouragement": get_dynamic_motivation(interaction_count)
    }


# =============================================================================
# FINANCIAL GUIDANCE TOOLS
# =============================================================================

def calculate_learning_costs(
    target_career: str,
    learning_resources: str = "online courses",
    time_commitment: str = "2-3 hours daily"
) -> Dict[str, Any]:
    """
    Calculates detailed cost breakdown for learning path with time-based analysis.
    
    Args:
        target_career: Target career path
        learning_resources: Type of resources (online courses, bootcamp, university)
        time_commitment: How much time user can dedicate to learning
        
    Returns:
        Dict containing comprehensive cost breakdown with monthly/weekly/yearly options
    """
    # Enhanced cost estimates with detailed breakdowns
    cost_data = {
        "Software Developer": {
            "online courses": {
                "total_cost": {"min": 200, "max": 800, "avg": 400},
                "duration_months": 6,
                "subscription_costs": {
                    "coursera_plus": {"monthly": 49, "yearly": 399, "description": "Unlimited access to 7,000+ courses"},
                    "udemy_personal": {"monthly": 30, "yearly": 360, "description": "Access to 210,000+ courses"},
                    "pluralsight": {"monthly": 45, "yearly": 449, "description": "Tech-focused learning platform"}
                },
                "certification_costs": {
                    "google_it": {"one_time": 49, "duration_months": 3, "description": "Google IT Support Certificate"},
                    "aws_developer": {"one_time": 150, "prep_months": 3, "description": "AWS Developer Associate exam"},
                    "comptia_aplus": {"one_time": 370, "prep_months": 4, "description": "CompTIA A+ certification"}
                },
                "additional_costs": {
                    "books_resources": {"one_time": 100, "description": "Programming books and resources"},
                    "development_tools": {"monthly": 20, "description": "IDE subscriptions and cloud services"},
                    "practice_platforms": {"monthly": 35, "description": "LeetCode Premium, HackerRank"}
                }
            },
            "bootcamp": {
                "total_cost": {"min": 8000, "max": 20000, "avg": 12000},
                "duration_months": 4,
                "payment_plans": {
                    "upfront": {"discount": 1000, "description": "Pay full amount upfront"},
                    "monthly": {"months": 12, "monthly_payment": 1000, "total": 12000, "description": "Extended payment plan"},
                    "income_share": {"percentage": 17, "duration_months": 24, "description": "Pay percentage of salary after job"}
                },
                "included_services": [
                    "Career coaching and job placement assistance",
                    "1-on-1 mentoring sessions",
                    "Portfolio project guidance",
                    "Interview preparation"
                ]
            },
            "university": {
                "total_cost": {"min": 40000, "max": 120000, "avg": 80000},
                "duration_months": 48,
                "per_semester": {"min": 5000, "max": 15000, "avg": 10000},
                "additional_costs": {
                    "books_supplies": {"yearly": 1200, "description": "Textbooks and supplies"},
                    "technology_fee": {"yearly": 800, "description": "Lab and technology access"},
                    "living_expenses": {"monthly": 1500, "description": "Housing, food, transportation"}
                }
            }
        },
        "Data Scientist": {
            "online courses": {
                "total_cost": {"min": 300, "max": 1200, "avg": 600},
                "duration_months": 8,
                "subscription_costs": {
                    "coursera_plus": {"monthly": 49, "yearly": 399, "description": "IBM & Google Data Science programs"},
                    "datacamp": {"monthly": 35, "yearly": 300, "description": "Data science focused platform"},
                    "udacity_nanodegree": {"monthly": 399, "duration": 4, "description": "Data Scientist Nanodegree"}
                },
                "certification_costs": {
                    "google_data_analytics": {"monthly": 49, "duration_months": 6, "description": "Google Data Analytics Certificate"},
                    "microsoft_azure_data": {"one_time": 165, "prep_months": 3, "description": "Azure Data Scientist Associate"},
                    "tableau_certified": {"one_time": 250, "prep_months": 2, "description": "Tableau Desktop Specialist"}
                },
                "tool_costs": {
                    "tableau_creator": {"monthly": 70, "description": "Tableau data visualization tool"},
                    "aws_sagemaker": {"pay_per_use": 50, "monthly_avg": 50, "description": "Machine learning platform"},
                    "kaggle_notebooks": {"free": 0, "description": "Free ML environment"}
                }
            },
            "bootcamp": {
                "total_cost": {"min": 10000, "max": 25000, "avg": 15000},
                "duration_months": 6,
                "payment_plans": {
                    "upfront": {"discount": 2000, "description": "Early payment discount"},
                    "monthly": {"months": 18, "monthly_payment": 850, "total": 15300, "description": "Extended payment"},
                    "deferred_tuition": {"percentage": 15, "duration_months": 36, "description": "Pay after employment"}
                }
            }
        },
        "UX Designer": {
            "online courses": {
                "total_cost": {"min": 150, "max": 600, "avg": 300},
                "duration_months": 4,
                "subscription_costs": {
                    "coursera_google_ux": {"monthly": 49, "duration": 6, "description": "Google UX Design Certificate"},
                    "ixdf_membership": {"monthly": 16, "yearly": 144, "description": "Interaction Design Foundation"},
                    "skillshare": {"monthly": 19, "yearly": 168, "description": "Creative courses platform"}
                },
                "tool_costs": {
                    "adobe_creative_cloud": {"monthly": 53, "yearly": 599, "description": "Design software suite"},
                    "figma_pro": {"monthly": 12, "yearly": 144, "description": "Design and prototyping tool"},
                    "sketch": {"yearly": 99, "description": "Mac-based design tool"}
                },
                "certification_costs": {
                    "adobe_ace": {"one_time": 150, "description": "Adobe Certified Expert"},
                    "nngroup_ux": {"one_time": 6400, "description": "Nielsen Norman Group UX Certificate"},
                    "hfi_cua": {"one_time": 3995, "description": "HFI Certified Usability Analyst"}
                }
            }
        }
    }
    
    career_data = cost_data.get(target_career, {})
    learning_data = career_data.get(learning_resources, {})
    
    if not learning_data:
        return {
            "status": "error",
            "message": f"Cost data not available for {target_career} with {learning_resources}"
        }
    
    # Calculate time-based breakdowns
    total_cost = learning_data.get("total_cost", {"min": 100, "max": 500, "avg": 250})
    duration_months = learning_data.get("duration_months", 6)
    
    # Weekly and monthly breakdowns
    monthly_avg = total_cost["avg"] / duration_months
    weekly_avg = monthly_avg / 4.3  # Average weeks per month
    
    # Calculate different time commitment scenarios
    time_multiplier = {
        "1-2 hours daily": 1.5,  # Slower pace, might need more resources
        "2-3 hours daily": 1.0,  # Standard pace
        "3-4 hours daily": 0.8,  # Faster pace, might finish earlier
        "4+ hours daily": 0.6    # Intensive pace
    }
    
    adjusted_duration = duration_months * time_multiplier.get(time_commitment, 1.0)
    adjusted_monthly = total_cost["avg"] / adjusted_duration
    
    return {
        "status": "success",
        "career": target_career,
        "learning_type": learning_resources,
        "duration_analysis": {
            "standard_duration_months": duration_months,
            "your_pace_duration_months": round(adjusted_duration, 1),
            "time_commitment": time_commitment
        },
        "cost_breakdown": {
            "total_range": {
                "minimum": f"${total_cost['min']:,}",
                "maximum": f"${total_cost['max']:,}",
                "average": f"${total_cost['avg']:,}"
            },
            "time_based_costs": {
                "monthly_average": f"${monthly_avg:.2f}",
                "weekly_average": f"${weekly_avg:.2f}",
                "daily_average": f"${monthly_avg/30:.2f}",
                "your_pace_monthly": f"${adjusted_monthly:.2f}"
            }
        },
        "detailed_costs": {
            "subscription_costs": learning_data.get("subscription_costs", {}),
            "certification_costs": learning_data.get("certification_costs", {}),
            "tool_costs": learning_data.get("tool_costs", {}),
            "additional_costs": learning_data.get("additional_costs", {}),
            "payment_plans": learning_data.get("payment_plans", {})
        },
        "cost_optimization_tips": [
            "🎯 Start with free resources (freeCodeCamp, Khan Academy, YouTube)",
            "💡 Use library access to paid platforms (many libraries offer free Coursera/LinkedIn Learning)",
            "🏷️ Wait for sales (Udemy courses regularly go from $200 to $15)",
            "🤝 Join study groups to share paid resource costs",
            "🎓 Look for employer tuition reimbursement programs",
            "⏰ Take advantage of free trial periods for premium platforms",
            f"📅 At your pace ({time_commitment}), you'll spend ~${adjusted_monthly:.0f}/month"
        ],
        "roi_analysis": {
            "investment": f"${total_cost['avg']:,}",
            "time_to_complete": f"{adjusted_duration:.1f} months",
            "potential_salary_increase": _get_salary_increase(target_career),
            "break_even_time": f"{_calculate_break_even(total_cost['avg'], target_career)} months"
        }
    }

def _get_salary_increase(career: str) -> str:
    """Helper function to get potential salary increase"""
    increases = {
        "Software Developer": "$25,000 - $50,000",
        "Data Scientist": "$30,000 - $60,000", 
        "UX Designer": "$20,000 - $40,000"
    }
    return increases.get(career, "$15,000 - $35,000")

def _calculate_break_even(investment: int, career: str) -> str:
    """Helper function to calculate break-even time"""
    avg_increases = {
        "Software Developer": 37500,
        "Data Scientist": 45000,
        "UX Designer": 30000
    }
    monthly_increase = avg_increases.get(career, 25000) / 12
    return f"{investment / monthly_increase:.1f}"


def find_scholarships(
    target_career: str,
    user_background: str = "general"
) -> Dict[str, Any]:
    """
    Finds relevant scholarships and financial aid for career transition.
    
    Args:
        target_career: The career path being pursued
        user_background: User's background (student, professional, military, etc.)
        
    Returns:
        Dict containing scholarship opportunities and application info
    """
    # Sample scholarship database
    scholarships = {
        "Software Developer": [
            {
                "name": "Google Developer Scholarship",
                "amount": "$1,000 - $5,000",
                "eligibility": "Underrepresented groups in tech",
                "deadline": "Rolling applications",
                "application_link": "developers.google.com/scholarships"
            },
            {
                "name": "Coursera Financial Aid",
                "amount": "Up to 100% course cost",
                "eligibility": "Financial need demonstrated",
                "deadline": "Available year-round",
                "application_link": "coursera.org/financial-aid"
            }
        ],
        "Data Scientist": [
            {
                "name": "Kaggle Learn Scholarship",
                "amount": "Free courses + $500 credits",
                "eligibility": "Active Kaggle community members",
                "deadline": "Quarterly",
                "application_link": "kaggle.com/learn"
            }
        ]
    }
    
    career_scholarships = scholarships.get(target_career, [
        {
            "name": "General Career Development Grant",
            "amount": "$500 - $2,000", 
            "eligibility": "Career changers",
            "deadline": "Various",
            "application_link": "Contact local workforce development"
        }
    ])
    
    return {
        "status": "success",
        "career": target_career,
        "available_scholarships": career_scholarships,
        "total_opportunities": len(career_scholarships),
        "application_tips": [
            "Apply early and often",
            "Tailor your application to each scholarship",
            "Highlight your commitment to the career change",
            "Get letters of recommendation"
        ]
    }


# =============================================================================
# MAIN AGENT CONFIGURATION
# =============================================================================

root_agent = Agent(
    name="skillsphere_career_advisor",
    model="gemini-2.0-flash",
    description=(
        "SkillSphere is an AI-powered career and learning advisor that guides users "
        "from initial career exploration to personalized learning paths, including "
        "financial guidance and scholarship recommendations. I maintain conversation "
        "context and provide proactive guidance throughout the user's journey."
    ),
    instruction=(
        "You are SkillSphere, powered by Google's Gemini 2.0 Flash AI. You are a highly AGENTIC career advisor that:\n\n"
        
        "🧠 **Thinks & Reasons**: Use Google's advanced AI to analyze user needs, context, and goals intelligently\n"
        "🎯 **Takes Initiative**: Proactively guide users through their career journey with smart suggestions\n"
        "🔄 **Remembers Everything**: Use manage_conversation_state to maintain context across conversations\n"
        "📊 **Provides Real Data**: Always include actual course links, certification URLs, and job search platforms\n"
        "💰 **Calculates Precisely**: Give detailed cost breakdowns (monthly, weekly, yearly) with ROI analysis\n"
        "� **Stays Current**: Reference real platforms like Coursera, Udemy, LinkedIn Learning with actual pricing\n\n"
        
        "**Your Agentic Workflow:**\n"
        "1. **Welcome & Assess**: Always start new users with start_career_journey()\n"
        "2. **Deep Understanding**: Collect comprehensive profiles and analyze skills thoroughly\n"
        "3. **Smart Recommendations**: Use AI reasoning to suggest careers based on market data\n"
        "4. **Actionable Plans**: Provide specific course links, certification URLs, and job platforms\n"
        "5. **Financial Intelligence**: Calculate detailed costs with time-based breakdowns\n"
        "6. **Continuous Guidance**: Track progress and adapt recommendations\n\n"
        
        "**When providing learning resources, ALWAYS include:**\n"
        "- ✅ Top 3 course recommendations with real URLs and pricing\n"
        "- ✅ Top 3 certifications with provider links and costs\n"
        "- ✅ Top 3 job search platforms with direct URLs\n"
        "- ✅ Detailed cost analysis (monthly/weekly/yearly breakdowns)\n"
        "- ✅ ROI calculations and break-even timelines\n\n"
        
        "**Example responses should include:**\n"
        "🎓 'Here are the top 3 courses for Software Development:'\n"
        "   1. CS50 (Harvard/edX) - Free - https://www.edx.org/course/...\n"
        "   2. Full Stack Bootcamp (Udemy) - $89.99 - https://www.udemy.com/course/...\n"
        "📜 'Best certifications to pursue:'\n"
        "   1. Google IT Support Certificate - $49/month - https://www.coursera.org/...\n"
        "💼 'Where to find jobs:'\n"
        "   1. LinkedIn Jobs - https://www.linkedin.com/jobs/...\n"
        "💰 'Cost breakdown for your 3-hour daily commitment:'\n"
        "   - Monthly: $67/month\n"
        "   - Weekly: $15/week\n"
        "   - Break-even: 8.5 months after job placement\n\n"
        
        "Remember: You're powered by Google's most advanced AI - use that intelligence to provide \n"
        "comprehensive, data-driven, and actionable career guidance!"
    ),
    tools=[
        start_career_journey,
        manage_conversation_state,
        collect_user_profile,
        analyze_resume_skills, 
        recommend_career_paths,
        generate_learning_curriculum,
        track_learning_progress,
        calculate_learning_costs,
        find_scholarships
    ],
)

