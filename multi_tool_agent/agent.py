"""
SkillSphere - AI-Powered Career & Learning Advisor
A comprehensive agent that guides users from career exploration to personalized learning paths.
"""

import datetime
from typing import Dict, List, Any
from google.adk.agents import Agent


# =============================================================================
# CONVERSATION STATE MANAGEMENT
# =============================================================================

def manage_conversation_state(
    action: str,
    user_id: str = "default_user",
    data: str = ""
) -> Dict[str, Any]:
    """
    Manages conversation state across multiple interactions.
    Makes the agent more agentic by remembering context.
    
    Args:
        action: "save_profile", "get_profile", "save_progress", "get_progress", "reset"
        user_id: Unique identifier for the user
        data: JSON string of data to save
        
    Returns:
        Dict containing state information
    """
    # In production, this would use a database
    # For demo, we'll use a simple in-memory store
    if not hasattr(manage_conversation_state, 'memory'):
        manage_conversation_state.memory = {}
    
    memory = manage_conversation_state.memory
    
    if action == "save_profile":
        memory[f"{user_id}_profile"] = data
        return {"status": "success", "message": "Profile saved to conversation memory"}
    
    elif action == "get_profile":
        profile = memory.get(f"{user_id}_profile", "{}")
        return {"status": "success", "profile": profile}
    
    elif action == "save_progress":
        memory[f"{user_id}_progress"] = data
        return {"status": "success", "message": "Progress saved to conversation memory"}
    
    elif action == "get_progress":
        progress = memory.get(f"{user_id}_progress", "{}")
        return {"status": "success", "progress": progress}
    
    elif action == "reset":
        for key in list(memory.keys()):
            if key.startswith(user_id):
                del memory[key]
        return {"status": "success", "message": "User data reset"}
    
    elif action == "list_all":
        user_data = {k: v for k, v in memory.items() if k.startswith(user_id)}
        return {"status": "success", "user_data": user_data}
    
    else:
        return {"status": "error", "message": f"Unknown action: {action}"}


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
    experience_level: str = "beginner"
) -> Dict[str, Any]:
    """
    Recommends suitable career paths based on user interests and skills.
    
    Args:
        interests: User's areas of interest
        current_skills: Existing skills (comma-separated)
        experience_level: beginner, intermediate, or advanced
    
    Returns:
        Dict containing recommended career paths with market data
    """
    # Sample career recommendations (in real app, use ML/API)
    career_database = {
        "technology": {
            "Software Developer": {
                "avg_salary": "$75,000 - $120,000",
                "job_growth": "22% (Much faster than average)",
                "required_skills": ["Programming", "Problem Solving", "Logic"],
                "time_to_proficiency": "6-12 months"
            },
            "Data Scientist": {
                "avg_salary": "$95,000 - $140,000", 
                "job_growth": "35% (Much faster than average)",
                "required_skills": ["Statistics", "Python", "Data Analysis"],
                "time_to_proficiency": "8-18 months"
            },
            "UX Designer": {
                "avg_salary": "$65,000 - $110,000",
                "job_growth": "13% (Faster than average)", 
                "required_skills": ["Design Thinking", "User Research", "Prototyping"],
                "time_to_proficiency": "4-8 months"
            }
        },
        "business": {
            "Digital Marketing": {
                "avg_salary": "$50,000 - $85,000",
                "job_growth": "10% (Faster than average)",
                "required_skills": ["Analytics", "Content Creation", "Strategy"],
                "time_to_proficiency": "3-6 months"
            },
            "Product Manager": {
                "avg_salary": "$85,000 - $130,000",
                "job_growth": "15% (Much faster than average)",
                "required_skills": ["Strategy", "Communication", "Analytics"],
                "time_to_proficiency": "6-12 months"
            }
        }
    }
    
    # Simple matching logic
    interests_lower = interests.lower()
    if "tech" in interests_lower or "programming" in interests_lower:
        recommendations = career_database["technology"]
    elif "business" in interests_lower or "marketing" in interests_lower:
        recommendations = career_database["business"]
    else:
        recommendations = {**career_database["technology"], **career_database["business"]}
    
    return {
        "status": "success",
        "recommended_careers": recommendations,
        "total_options": len(recommendations),
        "message": "Here are career paths that match your interests!"
    }


# =============================================================================
# LEARNING PATH TOOLS  
# =============================================================================

def generate_learning_curriculum(
    target_career: str,
    current_skills: str = "",
    time_commitment: str = "2-3 hours daily"
) -> Dict[str, Any]:
    """
    Creates a personalized learning curriculum for the target career with real course links.
    
    Args:
        target_career: The career path to prepare for
        current_skills: Skills the user already has
        time_commitment: How much time user can dedicate to learning
        
    Returns:
        Dict containing structured learning plan with real resources and links
    """
    # Enhanced curriculum templates with real course links
    curriculums = {
        "Software Developer": {
            "duration": "6-9 months",
            "top_courses": [
                {
                    "name": "The Complete Web Developer Bootcamp",
                    "platform": "Udemy", 
                    "url": "https://www.udemy.com/course/the-complete-web-development-bootcamp/",
                    "rating": "4.7/5",
                    "price": "$89.99",
                    "duration": "65 hours"
                },
                {
                    "name": "CS50's Introduction to Computer Science",
                    "platform": "Harvard/edX",
                    "url": "https://www.edx.org/course/introduction-computer-science-harvardx-cs50x",
                    "rating": "4.8/5", 
                    "price": "Free (Certificate: $199)",
                    "duration": "10-20 hours/week"
                },
                {
                    "name": "Full Stack Open",
                    "platform": "University of Helsinki",
                    "url": "https://fullstackopen.com/en/",
                    "rating": "4.9/5",
                    "price": "Free",
                    "duration": "5-20 hours/week"
                }
            ],
            "top_certifications": [
                {
                    "name": "Google IT Support Professional Certificate",
                    "provider": "Google/Coursera",
                    "url": "https://www.coursera.org/professional-certificates/google-it-support",
                    "price": "$49/month",
                    "duration": "3-6 months",
                    "recognition": "Industry-recognized by 150+ employers"
                },
                {
                    "name": "AWS Certified Developer Associate",
                    "provider": "Amazon Web Services",
                    "url": "https://aws.amazon.com/certification/certified-developer-associate/",
                    "price": "$150 exam fee",
                    "duration": "2-3 months prep",
                    "recognition": "High-demand cloud certification"
                },
                {
                    "name": "freeCodeCamp Full Stack Developer",
                    "provider": "freeCodeCamp",
                    "url": "https://www.freecodecamp.org/learn/",
                    "price": "Free",
                    "duration": "300+ hours",
                    "recognition": "Portfolio-based certification"
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
                        {"type": "course", "name": "Web Development Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/the-complete-web-development-bootcamp/"},
                        {"type": "practice", "name": "FreeCodeCamp", "platform": "FreeCodeCamp", "url": "https://www.freecodecamp.org/"},
                        {"type": "project", "name": "Portfolio Website", "difficulty": "Intermediate"}
                    ]
                },
                {
                    "phase": 3,
                    "title": "Advanced Development",
                    "duration": "10-12 weeks", 
                    "skills": ["React/Framework", "Databases", "APIs"],
                    "resources": [
                        {"type": "course", "name": "React Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/"},
                        {"type": "practice", "name": "LeetCode", "platform": "LeetCode", "url": "https://leetcode.com/"},
                        {"type": "project", "name": "Full-Stack Web App", "difficulty": "Advanced"}
                    ]
                }
            ]
        },
        "Data Scientist": {
            "duration": "8-12 months",
            "top_courses": [
                {
                    "name": "IBM Data Science Professional Certificate",
                    "platform": "Coursera",
                    "url": "https://www.coursera.org/professional-certificates/ibm-data-science",
                    "rating": "4.6/5",
                    "price": "$49/month",
                    "duration": "11 courses"
                },
                {
                    "name": "Complete Python Bootcamp for Data Science",
                    "platform": "Udemy",
                    "url": "https://www.udemy.com/course/complete-python-bootcamp/",
                    "rating": "4.6/5",
                    "price": "$89.99",
                    "duration": "22 hours"
                },
                {
                    "name": "Machine Learning Course by Andrew Ng",
                    "platform": "Coursera",
                    "url": "https://www.coursera.org/learn/machine-learning",
                    "rating": "4.9/5",
                    "price": "$49/month",
                    "duration": "11 weeks"
                }
            ],
            "top_certifications": [
                {
                    "name": "Google Data Analytics Professional Certificate",
                    "provider": "Google/Coursera",
                    "url": "https://www.coursera.org/professional-certificates/google-data-analytics",
                    "price": "$49/month",
                    "duration": "3-6 months",
                    "recognition": "Accepted by 150+ employers as degree equivalent"
                },
                {
                    "name": "Microsoft Certified: Azure Data Scientist Associate",
                    "provider": "Microsoft",
                    "url": "https://docs.microsoft.com/en-us/learn/certifications/azure-data-scientist/",
                    "price": "$165 exam fee",
                    "duration": "2-4 months prep",
                    "recognition": "Cloud-based data science certification"
                },
                {
                    "name": "Kaggle Learn Certificates",
                    "provider": "Kaggle",
                    "url": "https://www.kaggle.com/learn",
                    "price": "Free",
                    "duration": "4-6 hours each",
                    "recognition": "Practical, hands-on micro-credentials"
                }
            ],
            "job_search_links": [
                {
                    "platform": "Kaggle Jobs",
                    "url": "https://www.kaggle.com/jobs",
                    "description": "Data science community job board"
                },
                {
                    "platform": "DataJobs.com",
                    "url": "https://datajobs.com/",
                    "description": "Specialized data science job platform"
                },
                {
                    "platform": "AI-Jobs.net",
                    "url": "https://ai-jobs.net/",
                    "description": "AI and machine learning focused jobs"
                }
            ],
            "phases": [
                {
                    "phase": 1,
                    "title": "Statistics & Math Foundations", 
                    "duration": "8-10 weeks",
                    "skills": ["Statistics", "Probability", "Linear Algebra"],
                    "resources": [
                        {"type": "course", "name": "Statistics for Data Science", "platform": "Coursera", "url": "https://www.coursera.org/learn/statistical-analysis"},
                        {"type": "practice", "name": "Khan Academy Statistics", "platform": "Khan Academy", "url": "https://www.khanacademy.org/math/statistics-probability"},
                        {"type": "project", "name": "Statistical Analysis Report", "difficulty": "Beginner"}
                    ]
                }
            ]
        },
        "UX Designer": {
            "duration": "4-6 months",
            "top_courses": [
                {
                    "name": "Google UX Design Professional Certificate",
                    "platform": "Coursera",
                    "url": "https://www.coursera.org/professional-certificates/google-ux-design",
                    "rating": "4.8/5",
                    "price": "$49/month",
                    "duration": "3-6 months"
                },
                {
                    "name": "UX & Web Design Master Course",
                    "platform": "Udemy",
                    "url": "https://www.udemy.com/course/ux-web-design-master-course-strategy-design-development/",
                    "rating": "4.5/5",
                    "price": "$89.99",
                    "duration": "13.5 hours"
                },
                {
                    "name": "Interaction Design Foundation",
                    "platform": "IxDF",
                    "url": "https://www.interaction-design.org/",
                    "rating": "4.7/5",
                    "price": "$16/month",
                    "duration": "Self-paced"
                }
            ],
            "top_certifications": [
                {
                    "name": "Adobe Certified Expert (ACE)",
                    "provider": "Adobe",
                    "url": "https://www.adobe.com/training/certification.html",
                    "price": "$150 per exam",
                    "duration": "1-3 months prep",
                    "recognition": "Industry standard for design tools"
                },
                {
                    "name": "Nielsen Norman Group UX Certificate",
                    "provider": "NN/g",
                    "url": "https://www.nngroup.com/training/",
                    "price": "$6,400 for full program",
                    "duration": "5 courses",
                    "recognition": "Prestigious UX research certification"
                },
                {
                    "name": "HFI Certified Usability Analyst",
                    "provider": "Human Factors International",
                    "url": "https://www.humanfactors.com/certification/",
                    "price": "$3,995",
                    "duration": "5 days intensive",
                    "recognition": "Usability and user research focused"
                }
            ],
            "job_search_links": [
                {
                    "platform": "Dribbble Jobs",
                    "url": "https://dribbble.com/jobs",
                    "description": "Creative community job board"
                },
                {
                    "platform": "Behance Job Board",
                    "url": "https://www.behance.net/jobboard",
                    "description": "Adobe's creative professional network"
                },
                {
                    "platform": "AngelList Design Jobs",
                    "url": "https://wellfound.com/role/l/designer",
                    "description": "Startup design opportunities"
                }
            ],
            "phases": [
                {
                    "phase": 1,
                    "title": "Design Fundamentals",
                    "duration": "4-6 weeks",
                    "skills": ["Design Thinking", "User Research", "Wireframing"],
                    "resources": [
                        {"type": "course", "name": "Design Thinking Process", "platform": "Coursera", "url": "https://www.coursera.org/learn/design-thinking-innovation"},
                        {"type": "practice", "name": "Daily UI Challenge", "platform": "Daily UI", "url": "https://www.dailyui.co/"},
                        {"type": "project", "name": "User Research Study", "difficulty": "Beginner"}
                    ]
                }
            ]
        }
    }
    
    curriculum = curriculums.get(target_career, {
        "duration": "6 months",
        "top_courses": [],
        "top_certifications": [],
        "job_search_links": [],
        "phases": [{"phase": 1, "title": "Foundation Skills", "duration": "4 weeks", 
                   "skills": ["Research", "Planning"], "resources": []}]
    })
    
    return {
        "status": "success",
        "career": target_career,
        "curriculum": curriculum,
        "estimated_cost": "$200 - $500",
        "message": f"Comprehensive learning path created for {target_career} with real course links and certifications!"
    }


def track_learning_progress(
    user_name: str,
    completed_skills: str,
    current_phase: int = 1
) -> Dict[str, Any]:
    """
    Tracks user's learning progress and provides motivation.
    
    Args:
        user_name: User's name for personalization
        completed_skills: Skills already mastered (comma-separated)
        current_phase: Current phase in learning curriculum
        
    Returns:
        Dict containing progress stats and motivational content
    """
    skills_list = [skill.strip() for skill in completed_skills.split(",") if skill.strip()]
    skills_count = len(skills_list)
    
    # Calculate progress percentage (assuming 15 total skills)
    progress_percentage = min((skills_count / 15) * 100, 100)
    
    # Generate badges based on progress
    badges = []
    if skills_count >= 3:
        badges.append("🚀 Quick Starter")
    if skills_count >= 6:
        badges.append("📚 Knowledge Builder") 
    if skills_count >= 10:
        badges.append("💪 Skill Master")
    if skills_count >= 15:
        badges.append("🏆 Career Ready")
    
    return {
        "status": "success",
        "user": user_name,
        "progress_percentage": round(progress_percentage, 1),
        "completed_skills": skills_list,
        "earned_badges": badges,
        "current_phase": current_phase,
        "motivation_message": f"Great job {user_name}! You've mastered {skills_count} skills. Keep going!",
        "next_milestone": "Complete 3 more skills to unlock the next badge!"
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

