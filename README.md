# SkillSphere - a holistic view of your skills and future.

> Transform career uncertainty into a personalized, efficient, and cost-effective learning journey with AI-driven guidance.

[![Made with Google ADK](https://img.shields.io/badge/Made%20with-Google%20ADK-4285F4?style=flat-square&logo=google)](https://adk.googledemos.com/)
[![Powered by Gemini AI](https://img.shields.io/badge/Powered%20by-Gemini%20AI-34A853?style=flat-square)](https://ai.google.dev/)
[![Built with Flask](https://img.shields.io/badge/Built%20with-Flask-000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)

## Table of Contents
- [Problem Statement](#-problem-statement)
- [Our Solution](#-our-solution)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Development](#-development)
- [Contributing](#-contributing)
- [License](#-license)

## Problem Statement

Students and professionals struggle with career uncertainty and inefficient upskilling because traditional guidance is **generic, stereotypical, and disconnected from the job market**.

### Core Issues We Solve:
- **🎯 Poor Career Fit**: Individuals don't know which fields match their skills and interests
- **❓ Unclear Skill Gaps**: Lack of visibility into specific knowledge needed to advance
- **⏰ Wasted Learning Time**: Overwhelmed by resources without structured, personalized paths
- **💸 High Financial Risk**: Spending money with no guaranteed ROI
- **🎓 Education-Employment Mismatch**: Outdated curricula leaving workers underprepared

## Our Solution

SkillSphere provides a **data-driven AI platform** that transforms career uncertainty into a personalized, efficient, and cost-effective journey. Our solution acts as a dynamic digital career advisor, aligning individual potential with real-time job market demand.

| Problem | How We Solve It | Result for User |
|---------|-----------------|-----------------|
| **Poor Fit & Uncertainty** | Personalized AI Matching using CV/Resume analysis | **Clarity & Confidence** in career direction |
| **Unclear Skill Gaps** | Dynamic Gap Analysis comparing current vs. required skills | **Targeted Preparation** with specific learning goals |
| **Wasted Learning Time** | Structured Learning Paths with personalized curricula | **Efficiency & Focus** with accelerated learning |
| **High Financial Risk** | Cost-Optimized Education with scholarship recommendations | **Maximized ROI** with smart financial planning |
| **Education-Employment Mismatch** | Real-Time Market Feedback with salary and demand data | **Relevant & Employable** skills for immediate value |

## Features

### **AI-Powered Intelligence**
- **Agentic AI**: Powered by Google's Gemini 2.0 Flash for intelligent reasoning
- **Context Awareness**: Maintains conversation memory across sessions
- **Proactive Guidance**: AI takes initiative to suggest next steps

### **User Profiling & Analysis**
- Comprehensive profile collection (skills, interests, goals)
- Resume/CV analysis with skill extraction
- Learning style and time availability assessment

### **Career Recommendations**
- Data-driven career matching based on interests and skills
- Real salary data and job growth projections
- Market demand analysis with job posting frequency

### **Personalized Learning Paths**
- **Real Course Links**: Top 3 courses with actual URLs and pricing
- **Certification Guidance**: Industry-recognized credentials with provider links
- **Job Search Resources**: Direct links to relevant job platforms
- Phase-by-phase curriculum with specific milestones

### **Financial Planning**
- **Detailed Cost Analysis**: Monthly, weekly, yearly breakdowns
- **ROI Calculations**: Break-even time and salary increase projections
- **Scholarship Finder**: Targeted financial aid recommendations
- **Payment Plan Options**: Flexible learning investment strategies

### **Progress Tracking**
- Skill mastery badges and achievements
- Learning milestone tracking
- Motivational progress updates

## Architecture

```
Frontend (HTML/CSS/JS) → Backend (Flask) → Agent (ADK) → AI (Gemini 2.0 Flash)
```

### **Components:**
- **🎨 Frontend**: Professional web interface with real-time chat
- **⚙️ Backend**: Flask server with RESTful API endpoints
- **🧠 Agent**: Google ADK agent with specialized career tools
- **🔑 AI Engine**: Gemini 2.0 Flash for intelligent reasoning

## Quick Start

### **Prerequisites**
- Python 3.8+
- Google API Key (for Gemini AI)
- Google ADK installed

### **1. Clone & Setup**
```bash
git clone https://github.com/VJGit1/SkillSphere.git
cd SkillSphere
pip install -r requirements.txt
```

### **2. Configure Environment**
```bash
# Create .env file in multi_tool_agent/ directory
echo "GOOGLE_GENAI_USE_VERTEXAI=FALSE" > multi_tool_agent/.env
echo "GOOGLE_API_KEY=your_api_key_here" >> multi_tool_agent/.env
```

### **3. Run Application - Three Ways to Experience SkillSphere**

**Option A: Complete Application (Recommended for Demos)**
```bash
python server.py
# Visit: http://localhost:5000
# Professional UI with chat interface
```

**Option B: Streamlit Interface (User-Friendly)**
```bash
streamlit run streamlit_app.py
# Visit: http://localhost:8501
# Interactive web app with forms and widgets
```

**Option C: Agent Testing (Development)**
```bash
adk web
# Visit: http://localhost:8000
# Select 'multi_tool_agent' from dropdown
# Direct agent testing interface
```

## Installation

### **Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 2: Install Google ADK**
```bash
pip install google-adk
```

### **Step 3: Get Google API Key**
1. Visit [Google AI Studio](https://ai.google.dev/)
2. Create a new API key
3. Copy the key to your `.env` file

### **Step 4: Environment Setup**
Create `multi_tool_agent/.env`:
```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_actual_api_key_here
```

## Usage

### **Three Ways to Experience SkillSphere**

#### **1. Complete Application (Best for Hackathon Demos)**
```bash
python server.py
# Visit: http://localhost:5000
```
- **Features**: Professional chat interface, real-time responses
- **Best For**: Demonstrations, hackathon presentations
- **UI**: Custom HTML/CSS with agent integration

#### **2. Streamlit Interface (User-Friendly)**
```bash
streamlit run streamlit_app.py
# Visit: http://localhost:8501
```
- **Features**: Interactive forms, widgets, step-by-step guidance
- **Best For**: User testing, interactive exploration
- **UI**: Streamlit's native components with sidebar navigation

#### **3. ADK Agent Testing (Development)**
```bash
adk web
# Visit: http://localhost:8000
# Select 'multi_tool_agent' from the dropdown
```
- **Features**: Direct agent tool testing, function debugging
- **Best For**: Development, tool validation
- **UI**: ADK's default agent testing interface

### **All Three Provide Same Core Intelligence**
- ✅ Same Gemini 2.0 Flash AI model
- ✅ Same 9 career guidance tools
- ✅ Same real course links and cost calculations
- ✅ Same personalized recommendations

**Choose based on your audience:**
- **Judges/Demos**: Flask app (localhost:5000)
- **End Users**: Streamlit app (localhost:8501)  
- **Developers**: ADK web (localhost:8000)

### **Example Prompts to Try**

- **Career Exploration**: *"I'm a marketing graduate interested in technology. Help me find a career path."*
- **Learning Resources**: *"Show me the top 3 courses for software development with real links."*
- **Cost Analysis**: *"Calculate monthly costs for becoming a data scientist."*
- **Job Search**: *"Where can I find UX design jobs?"*

### **ADK Agent Testing (Development)**

```bash
adk web
# Visit: http://localhost:8000
# Select 'multi_tool_agent' from dropdown (as shown in screenshot)
# Test individual agent functions directly
```

**What you'll see:**
1. ADK web interface opens
2. Dropdown shows "multi_tool_agent" and "templates"
3. Select "multi_tool_agent" to test your SkillSphere agent
4. Direct access to all 9 career guidance tools

## API Documentation

### **Base URL**: `http://localhost:5000/api`

### **Endpoints**

#### **POST /api/chat**
Main chat endpoint for conversation with AI agent.

```json
{
  "message": "I want to become a software developer",
  "user_id": "unique_user_identifier"
}
```

**Response:**
```json
{
  "status": "success",
  "response": {
    "message": "Formatted response with course links",
    "suggestions": ["Calculate costs", "Find scholarships"],
    "type": "curriculum"
  }
}
```

#### **POST /api/start-journey**
Initialize a career guidance session.

```json
{
  "name": "Sarah",
  "user_id": "user_123"
}
```

#### **GET /health**
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "agent_loaded": true,
  "message": "SkillSphere backend is running"
}
```

## Development

### **Project Structure**
```
SkillSphere/
├── multi_tool_agent/
│   ├── agent.py          # Main ADK agent with career tools
│   ├── .env              # Google API key configuration
│   └── __init__.py       # Module initialization
├── templates/
│   └── index.html        # Frontend UI
├── server.py             # Flask backend server
├── streamlit_app.py      # Alternative Streamlit interface
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

### **Agent Tools**
- `start_career_journey()` - Welcome and initial guidance
- `collect_user_profile()` - Comprehensive profile collection
- `analyze_resume_skills()` - Resume/CV skill extraction
- `recommend_career_paths()` - AI-powered career matching
- `generate_learning_curriculum()` - Personalized learning paths
- `track_learning_progress()` - Progress monitoring with badges
- `calculate_learning_costs()` - Detailed financial analysis
- `find_scholarships()` - Targeted scholarship recommendations
- `manage_conversation_state()` - Session memory management

### **Testing the Agent**

1. **Individual Tool Testing**
   ```bash
   adk web
   # Test: "Start my career journey"
   # Test: "Analyze my resume: [paste resume text]"
   # Test: "Recommend careers for technology interests"
   ```

2. **Complete Flow Testing**
   ```bash
   python server.py
   # Test full user journey from profile to job placement
   ```

### **Adding New Features**

1. **New Agent Tool**
   ```python
   def new_career_tool(parameter: str) -> Dict[str, Any]:
       """New tool description"""
       return {"status": "success", "data": "result"}
   ```

2. **Add to Agent**
   ```python
   tools=[..., new_career_tool]
   ```

3. **Update Server Route**
   ```python
   # Add keyword detection in call_agent_sync()
   elif 'new_feature' in message_lower:
       result = new_career_tool(parameter)
   ```

## Deployment Options

### **Local Development**
```bash
python server.py  # Development server
```

### **Production Deployment**
```bash
# Using Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 server:app

# Using Docker
docker build -t skillsphere .
docker run -p 5000:5000 skillsphere
```

### **Cloud Deployment**
- **Google Cloud Run**: Deploy with ADK integration
- **Heroku**: Easy deployment with Procfile
- **AWS EC2**: Full control deployment
- **Streamlit Cloud**: For Streamlit version

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md).

### **Development Setup**
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Hackathon Information

**Project**: SkillSphere - AI Career Advisor  
**Team**: VB  
**Technology Stack**: Google ADK, Gemini AI, Flask, HTML/CSS/JS  
**Demo URL**: http://localhost:5000  

### **Key Innovation Points**
- ✅ Real-time AI agent powered by Google's latest Gemini model
- ✅ Actual course links and certification URLs (not mock data)
- ✅ Detailed financial analysis with ROI calculations
- ✅ Agentic AI that takes initiative and maintains context
- ✅ Professional UI with seamless agent integration

## Acknowledgments

- **Google ADK Team** for the powerful agent development framework
- **Google AI** for Gemini 2.0 Flash model access
- **Course Providers** (Coursera, Udemy, edX) for educational resources
- **Open Source Community** for inspiration and tools


---

**Made with ❤️ for career transformation through AI**
