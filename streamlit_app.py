"""
SkillSphere - Streamlit Frontend
AI-Powered Career & Learning Advisor Interface
"""

import streamlit as st
import requests
import json
from datetime import datetime
import sys
import os

# Add the current directory to Python path to import the agent
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Try to import the agent directly (for direct integration)
try:
    from agent import root_agent
    DIRECT_AGENT = True
except ImportError:
    DIRECT_AGENT = False
    st.error("Could not import agent directly. Make sure agent.py is in the same directory.")

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================

st.set_page_config(
    page_title="SkillSphere - AI Career Advisor",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .progress-badge {
        background: #28a745;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        margin: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def call_agent_tool(tool_name: str, **kwargs):
    """Call agent tools directly if available, otherwise use API"""
    if DIRECT_AGENT:
        try:
            # Get the tool function from the agent
            tools = {
                'collect_user_profile': collect_user_profile,
                'analyze_resume_skills': analyze_resume_skills,
                'recommend_career_paths': recommend_career_paths,
                'generate_learning_curriculum': generate_learning_curriculum,
                'track_learning_progress': track_learning_progress,
                'calculate_learning_costs': calculate_learning_costs,
                'find_scholarships': find_scholarships
            }
            
            # Import the functions from agent module
            from agent import (
                collect_user_profile, analyze_resume_skills, recommend_career_paths,
                generate_learning_curriculum, track_learning_progress,
                calculate_learning_costs, find_scholarships
            )
            
            tool_func = tools.get(tool_name)
            if tool_func:
                return tool_func(**kwargs)
            else:
                return {"status": "error", "message": f"Tool {tool_name} not found"}
        except Exception as e:
            return {"status": "error", "message": f"Error calling tool: {str(e)}"}
    else:
        return {"status": "error", "message": "Direct agent integration not available"}

def initialize_session_state():
    """Initialize session state variables"""
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = None
    if 'current_skills' not in st.session_state:
        st.session_state.current_skills = []
    if 'recommended_careers' not in st.session_state:
        st.session_state.recommended_careers = None
    if 'learning_plan' not in st.session_state:
        st.session_state.learning_plan = None
    if 'progress_data' not in st.session_state:
        st.session_state.progress_data = None

# =============================================================================
# MAIN APPLICATION
# =============================================================================

def main():
    initialize_session_state()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎯 SkillSphere</h1>
        <h3>AI-Powered Career & Learning Advisor</h3>
        <p>Transform career uncertainty into a personalized, efficient learning journey</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for navigation
    with st.sidebar:
        st.title("🧭 Navigation")
        page = st.selectbox(
            "Choose Your Journey:",
            ["🏠 Home", "👤 Profile Setup", "📊 Skill Analysis", "🎯 Career Recommendations", 
             "📚 Learning Path", "📈 Progress Tracking", "💰 Financial Planning"]
        )
        
        st.markdown("---")
        st.markdown("### 🌟 Your Progress")
        if st.session_state.user_profile:
            st.success("✅ Profile Created")
        if st.session_state.current_skills:
            st.success("✅ Skills Analyzed")
        if st.session_state.recommended_careers:
            st.success("✅ Careers Recommended")
        if st.session_state.learning_plan:
            st.success("✅ Learning Plan Created")
    
    # Main content based on selected page
    if page == "🏠 Home":
        show_home_page()
    elif page == "👤 Profile Setup":
        show_profile_setup()
    elif page == "📊 Skill Analysis":
        show_skill_analysis()
    elif page == "🎯 Career Recommendations":
        show_career_recommendations()
    elif page == "📚 Learning Path":
        show_learning_path()
    elif page == "📈 Progress Tracking":
        show_progress_tracking()
    elif page == "💰 Financial Planning":
        show_financial_planning()

def show_home_page():
    """Display the home page with problem statement and solution"""
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
        <h3>🎯 The Problem We Solve</h3>
        <ul>
        <li><strong>Poor Career Fit:</strong> Unclear which fields match your skills</li>
        <li><strong>Skill Gaps:</strong> Don't know what to learn next</li>
        <li><strong>Wasted Time:</strong> Overwhelmed by resources</li>
        <li><strong>Financial Risk:</strong> High costs, uncertain ROI</li>
        <li><strong>Education Mismatch:</strong> Outdated curricula</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
        <h3>✨ Our Solution</h3>
        <ul>
        <li><strong>AI Matching:</strong> Personalized career recommendations</li>
        <li><strong>Gap Analysis:</strong> Precise skill requirements</li>
        <li><strong>Structured Paths:</strong> Hyper-personalized curricula</li>
        <li><strong>Cost Optimization:</strong> Scholarship recommendations</li>
        <li><strong>Real-Time Data:</strong> Market-driven insights</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🚀 Get Started")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("👤 Create Profile", use_container_width=True):
            st.session_state.page = "👤 Profile Setup"
            st.rerun()
    
    with col2:
        if st.button("📊 Analyze Skills", use_container_width=True):
            st.session_state.page = "📊 Skill Analysis"
            st.rerun()
    
    with col3:
        if st.button("🎯 Find Careers", use_container_width=True):
            st.session_state.page = "🎯 Career Recommendations"
            st.rerun()

def show_profile_setup():
    """Profile creation interface"""
    st.header("👤 Create Your Profile")
    
    with st.form("profile_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name", placeholder="e.g., Sarah Johnson")
            current_role = st.text_input("Current Role", placeholder="e.g., Marketing Coordinator")
            experience_years = st.slider("Years of Experience", 0, 20, 2)
        
        with col2:
            interests = st.text_area("Interests & Passions", 
                                   placeholder="e.g., technology, design, problem-solving")
            learning_style = st.selectbox("Learning Style", 
                                        ["visual", "auditory", "hands-on", "reading"])
            time_availability = st.selectbox("Time Availability", 
                                           ["1-2 hours daily", "2-3 hours daily", 
                                            "3-4 hours daily", "4+ hours daily"])
        
        submitted = st.form_submit_button("Create Profile", use_container_width=True)
        
        if submitted and name:
            with st.spinner("Creating your profile..."):
                result = call_agent_tool(
                    "collect_user_profile",
                    name=name,
                    current_role=current_role,
                    experience_years=experience_years,
                    interests=interests,
                    learning_style=learning_style,
                    time_availability=time_availability
                )
                
                if result.get("status") == "success":
                    st.session_state.user_profile = result.get("profile")
                    st.success(result.get("message"))
                    st.balloons()
                else:
                    st.error(f"Error: {result.get('message', 'Unknown error')}")

def show_skill_analysis():
    """Resume/skill analysis interface"""
    st.header("📊 Analyze Your Skills")
    
    resume_text = st.text_area(
        "Paste Your Resume/CV Content:",
        height=200,
        placeholder="Paste your resume content here or describe your experience..."
    )
    
    if st.button("Analyze Skills", use_container_width=True):
        if resume_text:
            with st.spinner("Analyzing your skills..."):
                result = call_agent_tool("analyze_resume_skills", resume_text=resume_text)
                
                if result.get("status") == "success":
                    st.session_state.current_skills = result.get("current_skills", [])
                    
                    st.success("Skills analyzed successfully!")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("🎯 Identified Skills")
                        for skill in result.get("current_skills", []):
                            st.markdown(f"• {skill.title()}")
                    
                    with col2:
                        st.subheader("📈 Recommendations")
                        st.info(result.get("recommendations"))
                        st.success(result.get("next_step"))
                else:
                    st.error(f"Error: {result.get('message', 'Unknown error')}")
        else:
            st.warning("Please enter your resume content first.")

def show_career_recommendations():
    """Career recommendation interface"""
    st.header("🎯 Career Recommendations")
    
    if not st.session_state.user_profile:
        st.warning("Please create your profile first in the Profile Setup section.")
        return
    
    profile = st.session_state.user_profile
    interests = ", ".join(profile.get("interests", []))
    current_skills = ", ".join(st.session_state.current_skills)
    
    if st.button("Get Career Recommendations", use_container_width=True):
        with st.spinner("Analyzing market data and finding your perfect career fit..."):
            result = call_agent_tool(
                "recommend_career_paths",
                interests=interests,
                current_skills=current_skills,
                experience_level="beginner" if profile.get("experience_years", 0) < 2 else "intermediate"
            )
            
            if result.get("status") == "success":
                st.session_state.recommended_careers = result.get("recommended_careers")
                
                st.success(f"Found {result.get('total_options')} career matches!")
                st.info(result.get("message"))
                
                # Display career recommendations
                for career, details in result.get("recommended_careers", {}).items():
                    with st.expander(f"🚀 {career}", expanded=True):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.metric("Average Salary", details.get("avg_salary"))
                            st.metric("Job Growth", details.get("job_growth"))
                        
                        with col2:
                            st.subheader("Required Skills:")
                            for skill in details.get("required_skills", []):
                                st.markdown(f"• {skill}")
                            
                            st.subheader("Time to Proficiency:")
                            st.info(details.get("time_to_proficiency"))

def show_learning_path():
    """Learning curriculum interface"""
    st.header("📚 Personalized Learning Path")
    
    if not st.session_state.recommended_careers:
        st.warning("Please get career recommendations first.")
        return
    
    # Career selection
    career_options = list(st.session_state.recommended_careers.keys())
    selected_career = st.selectbox("Select Your Target Career:", career_options)
    
    current_skills = ", ".join(st.session_state.current_skills)
    profile = st.session_state.user_profile or {}
    time_commitment = profile.get("time_availability", "2-3 hours daily")
    
    if st.button("Generate Learning Plan", use_container_width=True):
        with st.spinner("Creating your personalized curriculum..."):
            result = call_agent_tool(
                "generate_learning_curriculum",
                target_career=selected_career,
                current_skills=current_skills,
                time_commitment=time_commitment
            )
            
            if result.get("status") == "success":
                st.session_state.learning_plan = result.get("curriculum")
                
                st.success(result.get("message"))
                
                curriculum = result.get("curriculum", {})
                
                # Display curriculum overview
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Duration", curriculum.get("duration"))
                with col2:
                    st.metric("Estimated Cost", result.get("estimated_cost"))
                
                # Display phases
                for phase in curriculum.get("phases", []):
                    with st.expander(f"Phase {phase.get('phase')}: {phase.get('title')}", expanded=True):
                        st.markdown(f"**Duration:** {phase.get('duration')}")
                        
                        st.subheader("Skills to Learn:")
                        for skill in phase.get("skills", []):
                            st.markdown(f"• {skill}")
                        
                        st.subheader("Resources:")
                        for resource in phase.get("resources", []):
                            st.markdown(f"• **{resource.get('type').title()}**: {resource.get('name')} ({resource.get('platform')})")

def show_progress_tracking():
    """Progress tracking interface"""
    st.header("📈 Track Your Progress")
    
    if not st.session_state.user_profile:
        st.warning("Please create your profile first.")
        return
    
    profile = st.session_state.user_profile
    
    completed_skills = st.text_area(
        "Skills You've Completed:",
        placeholder="e.g., Python basics, HTML, CSS, JavaScript fundamentals",
        help="Enter comma-separated list of skills you've mastered"
    )
    
    current_phase = st.slider("Current Learning Phase:", 1, 5, 1)
    
    if st.button("Update Progress", use_container_width=True):
        if completed_skills:
            with st.spinner("Calculating your progress..."):
                result = call_agent_tool(
                    "track_learning_progress",
                    user_name=profile.get("name"),
                    completed_skills=completed_skills,
                    current_phase=current_phase
                )
                
                if result.get("status") == "success":
                    st.session_state.progress_data = result
                    
                    # Progress display
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        progress = result.get("progress_percentage", 0)
                        st.metric("Progress", f"{progress}%")
                        st.progress(progress / 100)
                    
                    with col2:
                        st.metric("Skills Mastered", len(result.get("completed_skills", [])))
                        st.metric("Current Phase", result.get("current_phase"))
                    
                    with col3:
                        st.subheader("🏆 Badges Earned")
                        for badge in result.get("earned_badges", []):
                            st.markdown(f'<div class="progress-badge">{badge}</div>', 
                                      unsafe_allow_html=True)
                    
                    st.success(result.get("motivation_message"))
                    st.info(result.get("next_milestone"))

def show_financial_planning():
    """Financial planning interface"""
    st.header("💰 Financial Planning")
    
    if not st.session_state.recommended_careers:
        st.warning("Please get career recommendations first.")
        return
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💰 Cost Calculator")
        career_options = list(st.session_state.recommended_careers.keys())
        selected_career = st.selectbox("Career Path:", career_options)
        learning_type = st.selectbox("Learning Method:", ["online courses", "bootcamp"])
        
        if st.button("Calculate Costs"):
            result = call_agent_tool(
                "calculate_learning_costs",
                target_career=selected_career,
                learning_resources=learning_type
            )
            
            if result.get("status") == "success":
                costs = result.get("cost_breakdown", {})
                st.metric("Minimum Cost", costs.get("minimum"))
                st.metric("Average Cost", costs.get("average"))
                st.metric("Maximum Cost", costs.get("maximum"))
                
                st.subheader("💡 Cost Saving Tips:")
                for tip in result.get("cost_saving_tips", []):
                    st.markdown(f"• {tip}")
    
    with col2:
        st.subheader("🎓 Scholarship Finder")
        user_background = st.selectbox("Background:", ["general", "student", "professional", "military"])
        
        if st.button("Find Scholarships"):
            result = call_agent_tool(
                "find_scholarships",
                target_career=selected_career,
                user_background=user_background
            )
            
            if result.get("status") == "success":
                st.success(f"Found {result.get('total_opportunities')} opportunities!")
                
                for scholarship in result.get("available_scholarships", []):
                    with st.expander(scholarship.get("name")):
                        st.markdown(f"**Amount:** {scholarship.get('amount')}")
                        st.markdown(f"**Eligibility:** {scholarship.get('eligibility')}")
                        st.markdown(f"**Deadline:** {scholarship.get('deadline')}")
                        st.markdown(f"**Apply:** {scholarship.get('application_link')}")

if __name__ == "__main__":
    main()