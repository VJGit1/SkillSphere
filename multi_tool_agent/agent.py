"""
SkillSphere - AI-Powered Career & Learning Advisor
A comprehensive agent that guides users from career exploration to personalized learning paths.
"""

import datetime
from typing import Dict, List, Any
from google.adk.agents import Agent


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
    Creates a personalized learning curriculum for the target career.
    
    Args:
        target_career: The career path to prepare for
        current_skills: Skills the user already has
        time_commitment: How much time user can dedicate to learning
        
    Returns:
        Dict containing structured learning plan with resources
    """
    # Sample curriculum templates
    curriculums = {
        "Software Developer": {
            "duration": "6-9 months",
            "phases": [
                {
                    "phase": 1,
                    "title": "Programming Fundamentals",
                    "duration": "6-8 weeks",
                    "skills": ["Variables & Data Types", "Control Structures", "Functions"],
                    "resources": [
                        {"type": "course", "name": "Python for Beginners", "platform": "Coursera"},
                        {"type": "practice", "name": "HackerRank Python Track", "platform": "HackerRank"},
                        {"type": "project", "name": "Build a Calculator App", "difficulty": "Beginner"}
                    ]
                },
                {
                    "phase": 2, 
                    "title": "Web Development Basics",
                    "duration": "8-10 weeks",
                    "skills": ["HTML/CSS", "JavaScript", "Responsive Design"],
                    "resources": [
                        {"type": "course", "name": "Web Development Bootcamp", "platform": "Udemy"},
                        {"type": "practice", "name": "FreeCodeCamp", "platform": "FreeCodeCamp"},
                        {"type": "project", "name": "Portfolio Website", "difficulty": "Intermediate"}
                    ]
                },
                {
                    "phase": 3,
                    "title": "Advanced Development",
                    "duration": "10-12 weeks", 
                    "skills": ["React/Framework", "Databases", "APIs"],
                    "resources": [
                        {"type": "course", "name": "React Complete Guide", "platform": "Udemy"},
                        {"type": "practice", "name": "LeetCode", "platform": "LeetCode"},
                        {"type": "project", "name": "Full-Stack Web App", "difficulty": "Advanced"}
                    ]
                }
            ]
        },
        "Data Scientist": {
            "duration": "8-12 months",
            "phases": [
                {
                    "phase": 1,
                    "title": "Statistics & Math Foundations", 
                    "duration": "8-10 weeks",
                    "skills": ["Statistics", "Probability", "Linear Algebra"],
                    "resources": [
                        {"type": "course", "name": "Statistics for Data Science", "platform": "Coursera"},
                        {"type": "practice", "name": "Khan Academy Statistics", "platform": "Khan Academy"},
                        {"type": "project", "name": "Statistical Analysis Report", "difficulty": "Beginner"}
                    ]
                }
            ]
        }
    }
    
    curriculum = curriculums.get(target_career, {
        "duration": "6 months",
        "phases": [{"phase": 1, "title": "Foundation Skills", "duration": "4 weeks", 
                   "skills": ["Research", "Planning"], "resources": []}]
    })
    
    return {
        "status": "success",
        "career": target_career,
        "curriculum": curriculum,
        "estimated_cost": "$200 - $500",
        "message": f"Personalized learning path created for {target_career}!"
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
    learning_resources: str = "online courses"
) -> Dict[str, Any]:
    """
    Calculates estimated costs for learning path and suggests ways to reduce expenses.
    
    Args:
        target_career: Target career path
        learning_resources: Type of resources (online courses, bootcamp, university)
        
    Returns:
        Dict containing cost breakdown and savings suggestions
    """
    cost_estimates = {
        "online courses": {
            "Software Developer": {"min": 200, "max": 800, "avg": 400},
            "Data Scientist": {"min": 300, "max": 1200, "avg": 600}, 
            "UX Designer": {"min": 150, "max": 600, "avg": 300}
        },
        "bootcamp": {
            "Software Developer": {"min": 8000, "max": 20000, "avg": 12000},
            "Data Scientist": {"min": 10000, "max": 25000, "avg": 15000},
            "UX Designer": {"min": 6000, "max": 15000, "avg": 9000}
        }
    }
    
    costs = cost_estimates.get(learning_resources, {}).get(target_career, 
                                                          {"min": 100, "max": 500, "avg": 250})
    
    return {
        "status": "success", 
        "career": target_career,
        "learning_type": learning_resources,
        "cost_breakdown": {
            "minimum": f"${costs['min']}",
            "maximum": f"${costs['max']}", 
            "average": f"${costs['avg']}"
        },
        "cost_saving_tips": [
            "Look for free courses on Coursera and edX",
            "Use YouTube tutorials for supplementary learning",
            "Join study groups to share resource costs",
            "Apply for scholarships and financial aid"
        ]
    }


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
        "financial guidance and scholarship recommendations."
    ),
    instruction=(
        "You are SkillSphere, a friendly and knowledgeable career advisor. Your mission is to:\n\n"
        "1. **Understand the User**: Start by collecting their profile, interests, and goals\n"
        "2. **Recommend Careers**: Suggest suitable career paths based on their interests and market data\n"
        "3. **Create Learning Plans**: Design personalized curricula with specific resources and timelines\n"
        "4. **Track Progress**: Monitor their learning journey and provide motivation\n"
        "5. **Financial Guidance**: Help with cost planning and finding scholarships\n\n"
        "Always be encouraging, specific, and practical. Break complex information into digestible steps. "
        "Use the tools available to provide data-driven recommendations. "
        "Remember, you're helping someone make a life-changing career transition!"
    ),
    tools=[
        collect_user_profile,
        analyze_resume_skills, 
        recommend_career_paths,
        generate_learning_curriculum,
        track_learning_progress,
        calculate_learning_costs,
        find_scholarships
    ],
)

