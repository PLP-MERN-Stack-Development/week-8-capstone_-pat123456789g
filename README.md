# TajiAfya - Healthcare Management System
### Week 8 Capstone Project - PLP MERN Stack Development

![TajiAfya Hero](frontend/src/assets/hero-medical.jpg)

## 🏥 Project Overview

*TajiAfya* is a comprehensive healthcare management platform that bridges the gap between patients and healthcare providers in underserved communities. The name "TajiAfya" combines "Taji" (crown in Swahili) and "Afya" (health in Swahili), symbolizing crowned health - making quality healthcare accessible and dignified for everyone.

---

## 🎥 Project Pitch Video

*Watch our comprehensive project presentation:*

[![TajiAfya Pitch Deck](      )

📝 Note: Pitch deck video link will be updated shortly

Our pitch deck covers:
- 🎯 Problem identification and market opportunity
- 💡 TajiAfya's innovative solution approach
- 🏗 Technical architecture and implementation
- 📈 Business model and scalability plans
- 🌍 Social impact and future roadmap

---

## 🌐 Live Application

*Experience TajiAfya in action:*

[![Live Demo](   http://16.171.34.96/sign-in  )

📝 Note: Live application link will be updated shortly

*Application URLs:*
- 🎯 *Frontend*: [TajiAfya Web App](FRONTEND_LINK_HERE)
- 🔧 *API Backend*: [REST API Endpoints](BACKEND_API_LINK_HERE)
- 👨‍💼 *Admin Panel*: [Django Admin](ADMIN_PANEL_LINK_HERE)

Test the full functionality including user registration, symptom checker, medical records, and appointment booking.

---

## 🚀 Real-World Problem Statement

### The Challenge
Healthcare accessibility remains a critical challenge in many communities, particularly in developing regions where:

- *Limited Healthcare Access*: Remote areas lack sufficient medical facilities and specialists
- *Chronic Disease Management*: Patients struggle to monitor conditions like diabetes, hypertension, and heart disease without regular medical supervision
- *Delayed Diagnosis*: Symptom assessment and early detection are often delayed due to distance and cost barriers
- *Poor Record Management*: Medical records are often paper-based, leading to loss of critical health information
- *Appointment Scheduling*: Inefficient booking systems create long wait times and missed appointments

### Our Solution
TajiAfya addresses these challenges by providing:

1. *Digital Health Monitoring*: Real-time tracking of vital signs and symptoms
2. *AI-Powered Symptom Assessment*: Preliminary diagnosis assistance using intelligent symptom checking
3. *Telemedicine Integration*: Virtual consultations with healthcare providers
4. *Centralized Medical Records*: Secure, accessible digital health records
5. *Smart Appointment Management*: Efficient scheduling and reminder systems
6. *Chronic Disease Support*: Specialized tools for managing long-term health conditions

---

## 🎨 Wireframes and Mockups

### User Interface Design Philosophy
Our design follows a *medical-first* approach with:
- *Accessibility*: High contrast colors, readable fonts, and intuitive navigation
- *Trust*: Professional color scheme using medical blues and greens
- *Responsiveness*: Mobile-first design for accessibility in all environments

### Key Interface Components

#### 1. Landing Page

┌─────────────────────────────────────────────────┐
│ NAVIGATION: [Logo] [About] [Features] [Sign In] │
├─────────────────────────────────────────────────┤
│                  HERO SECTION                   │
│  [Medical Image] | "Your Health, Always         │
│                  │  Protected" - CTA Buttons    │
├─────────────────────────────────────────────────┤
│               SYMPTOM CHECKER                   │
│  Interactive assessment tool with progress bar  │
├─────────────────────────────────────────────────┤
│                  FEATURES                       │
│  [Health Monitor] [Appointments] [Records]      │
└─────────────────────────────────────────────────┘


#### 2. Patient Dashboard

┌─────────────────────────────────────────────────┐
│ HEADER: Welcome [Patient Name] | [Notifications]│
├─────────────────────────────────────────────────┤
│ QUICK STATS                                     │
│ [Last Checkup] [Next Appointment] [Medications] │
├─────────────────────────────────────────────────┤
│ MAIN CONTENT                                    │
│ ├─ Recent Medical Records                       │
│ ├─ Upcoming Appointments                        │
│ ├─ Health Metrics Charts                        │
│ └─ Emergency Contacts                           │
└─────────────────────────────────────────────────┘


#### 3. Symptom Checker Flow

Question 1 → Question 2 → Question 3 → Risk Assessment
    │            │            │              │
 [Progress]   [Progress]   [Progress]   [Results &
    Bar          Bar          Bar       Recommendations]


---

## 🗄 Database Schema and Relationships

### Entity Relationship Diagram

mermaid
erDiagram
    USER ||--o{ MEDICAL_RECORD : has
    USER ||--o{ APPOINTMENT : "books/provides"
    USER ||--o{ APPOINTMENT : "patient/doctor"
    MEDICAL_RECORD }o--|| USER : "created_by_doctor"
    
    USER {
        int id PK
        string username
        string email
        string password
        enum user_type
        string phone
        date birth_date
        datetime date_joined
        boolean is_active
        boolean is_staff
    }
    
    MEDICAL_RECORD {
        int id PK
        int patient_id FK
        int doctor_id FK
        text diagnosis
        text prescription
        datetime created_at
        datetime updated_at
    }
    
    APPOINTMENT {
        int id PK
        int patient_id FK
        int doctor_id FK
        datetime date_time
        enum status
        text notes
    }


### Database Models

#### 1. User Model (Custom Django User)
python
class User(AbstractUser):
    USER_TYPES = (
        ('P', 'Patient'),    # Regular patients
        ('D', 'Doctor'),     # Healthcare providers
        ('A', 'Admin'),      # System administrators
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPES)
    phone = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)


*Relationships:*
- One-to-many with MedicalRecord (as patient)
- One-to-many with MedicalRecord (as doctor)
- One-to-many with Appointment (as patient)
- One-to-many with Appointment (as doctor)

#### 2. Medical Record Model
python
class MedicalRecord(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='records')
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_records')
    diagnosis = models.TextField()
    prescription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


*Purpose:* Store patient medical history, diagnoses, and prescriptions

#### 3. Appointment Model
python
class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=(
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ))
    notes = models.TextField(blank=True)


*Purpose:* Manage patient-doctor appointments with status tracking

---

## 🔌 API Endpoints and Data Flow

### RESTful API Architecture

#### Authentication Endpoints

POST /api/register/          # User registration
POST /api/token/             # JWT token login
POST /api/token/refresh/     # Refresh JWT token


#### Core Application Endpoints

GET    /api/medical-records/ # List user's medical records
POST   /api/medical-records/ # Create new medical record
GET    /api/appointments/    # List user's appointments  
POST   /api/appointments/    # Book new appointment


### Data Flow Architecture

#### 1. User Authentication Flow

Frontend → POST /api/register → Backend → Database
    ↓
JWT Token Generated → Stored in Frontend → Used for API calls
    ↓
Protected Routes Access → Validated by JWT Middleware


#### 2. Medical Records Flow

Patient Dashboard → GET /api/medical-records → Django Backend
    ↓
Filter by patient → Query Database → Return JSON
    ↓
Frontend Rendering → Display in Dashboard Components


#### 3. Appointment Booking Flow

Appointment Form → POST /api/appointments → Validation
    ↓
Doctor Availability Check → Database Save → Confirmation
    ↓
Email/SMS Notification → Calendar Integration → Reminder System


#### 4. Symptom Checker Flow

Symptom Questions → Frontend Logic → Risk Assessment
    ↓
Recommendation Engine → Display Results → Optional Doctor Referral


### API Response Format
json
{
  "success": true,
  "data": {
    "medical_records": [
      {
        "id": 1,
        "diagnosis": "Type 2 Diabetes",
        "prescription": "Metformin 500mg twice daily",
        "created_at": "2024-01-15T10:30:00Z",
        "doctor": "Dr. Smith"
      }
    ]
  },
  "message": "Medical records retrieved successfully"
}


---

## 🗺 Project Roadmap and Milestones

### Phase 1: Foundation Setup ✅ *(Completed)*
*Timeline:* Week 1-2
- [x] Project initialization with React + TypeScript (Vite)
- [x] Django REST Framework backend setup
- [x] Database schema design and models
- [x] Basic authentication system (JWT)
- [x] UI component library integration (Shadcn/ui)

### Phase 2: Core Features Development ✅ *(Completed)*
*Timeline:* Week 3-4
- [x] User registration and login system
- [x] Patient dashboard creation
- [x] Medical records CRUD operations
- [x] Appointment booking system
- [x] Responsive design implementation

### Phase 3: Advanced Features 🚧 *(In Progress)*
*Timeline:* Week 5-6
- [x] Symptom checker implementation
- [ ] Real-time notifications
- [ ] Doctor dashboard
- [ ] Medical record search and filtering
- [ ] Appointment calendar integration

### Phase 4: Enhancement and Testing 📋 *(Planned)*
*Timeline:* Week 7-8
- [ ] Comprehensive testing suite
- [ ] Performance optimization
- [ ] Security audit and improvements
- [ ] Documentation completion
- [ ] Deployment preparation

### Phase 5: Production Deployment 🚀 *(Future)*
*Timeline:* Week 9+
- [ ] Cloud deployment (AWS/Heroku)
- [ ] CI/CD pipeline setup
- [ ] Production monitoring
- [ ] User feedback collection
- [ ] Feature iterations

### Milestone Tracking

Foundation    ████████████████████ 100%
Core Features ████████████████████ 100%  
Advanced      ████████████░░░░░░░░  65%
Testing       ░░░░░░░░░░░░░░░░░░░░   0%
Deployment    ░░░░░░░░░░░░░░░░░░░░   0%


---

## 🏗 Technical Architecture Decisions

### Frontend Architecture

#### *Technology Stack Choice: React + TypeScript + Vite*
*Decision Rationale:*
- *React*: Component-based architecture for reusable UI elements
- *TypeScript*: Type safety for robust healthcare data handling
- *Vite*: Fast development server and optimized builds
- *Tailwind CSS*: Utility-first CSS for rapid, consistent styling

#### *State Management: React Context + useState*
*Decision Rationale:*
- Medical apps require simple, predictable state management
- Context API sufficient for current scope
- Easy to migrate to Redux if complexity increases

#### *UI Components: Shadcn/ui + Radix UI*
*Decision Rationale:*
- Accessibility-first components (crucial for healthcare)
- Consistent design system
- Highly customizable with Tailwind CSS
- Professional appearance builds user trust

### Backend Architecture

#### *Framework Choice: Django REST Framework*
*Decision Rationale:*
- *Rapid Development*: Django's "batteries included" philosophy
- *Security*: Built-in protection against common vulnerabilities
- *Authentication*: Robust user management system
- *ORM*: Simplified database operations with complex relationships
- *Scalability*: Easy to scale with additional features

#### *Database: SQLite → PostgreSQL (Production)*
*Decision Rationale:*
- *Development*: SQLite for rapid prototyping
- *Production*: PostgreSQL for robust, scalable healthcare data storage
- *ACID Compliance*: Critical for medical record integrity
- *Relationship Support*: Complex medical data relationships

#### *Authentication: JWT (JSON Web Tokens)*
*Decision Rationale:*
- *Stateless*: Scalable authentication without server-side sessions
- *Security*: Token-based auth suitable for API-first architecture
- *Mobile Friendly*: Easy integration with mobile apps (future scope)

### Security Architecture

#### *Data Protection Measures*
1. *HTTPS Only*: All communications encrypted
2. *JWT Expiration*: Short-lived tokens with refresh mechanism
3. *CORS Configuration*: Restricted to known frontend origins
4. *Input Validation*: Comprehensive sanitization of user inputs
5. *Permission Classes*: Role-based access control (Patient/Doctor/Admin)

#### *Compliance Considerations*
- *GDPR Ready*: User data deletion and export capabilities
- *HIPAA Considerations*: Medical record access logging (planned)
- *Audit Trail*: Track all medical record modifications

### Performance Optimization

#### *Frontend Optimizations*
- *Code Splitting*: Lazy loading of dashboard components
- *Image Optimization*: WebP format with fallbacks
- *Bundle Analysis*: Regular monitoring of bundle size
- *Caching Strategy*: Service worker implementation (planned)

#### *Backend Optimizations*
- *Database Indexing*: Optimized queries for medical records
- *Pagination*: Efficient handling of large datasets
- *Serializer Optimization*: Minimal data transfer
- *Caching Layer*: Redis integration (planned)

### Scalability Considerations

#### *Horizontal Scaling Preparation*
- *Stateless Backend*: Easy to deploy multiple instances
- *Database Connection Pooling*: Efficient resource utilization
- *API Versioning*: Future-proof API design
- *Microservices Ready*: Modular architecture for service extraction

---

## 🛠 Technology Stack

### Frontend
- *React 18* with TypeScript
- *Vite* for fast development and building
- *Tailwind CSS* for styling
- *Shadcn/ui* component library
- *React Router* for navigation
- *Axios* for API communication
- *Lucide React* for icons

### Backend
- *Django 5.2* with Python
- *Django REST Framework* for API development
- *JWT Authentication* for security
- *SQLite* (development) / *PostgreSQL* (production)
- *CORS Headers* for cross-origin requests

### Development Tools
- *Git* for version control
- *ESLint* for code linting
- *Prettier* for code formatting
- *VS Code* as primary IDE
- *Postman* for API testing

---

## 🚦 Getting Started

### Prerequisites
- Node.js 18+ and npm/yarn
- Python 3.11+
- Git

### Installation

1. *Clone the repository*
bash
git clone https://github.com/PLP-MERN-Stack-Development/week-8-capstone_-pat123456789g.git
cd TajiAfya


2. *Install dependencies*
bash
npm run install-all


3. *Backend Setup*
bash
cd tajipatrick
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


4. *Frontend Setup*
bash
cd frontend
npm run dev


5. *Access the application*
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

---

## 🎯 Key Features

### For Patients
- ✅ *Health Dashboard*: Personal health overview and metrics
- ✅ *Symptom Checker*: AI-powered preliminary health assessment
- ✅ *Medical Records*: Secure access to personal health history
- ✅ *Appointment Booking*: Schedule consultations with healthcare providers
- 🚧 *Medication Reminders*: Track prescriptions and dosages
- 🚧 *Health Metrics Tracking*: Monitor vital signs and chronic conditions

### For Healthcare Providers
- ✅ *Patient Management*: View and manage patient records
- ✅ *Appointment Scheduling*: Manage consultation calendar
- 🚧 *Prescription Management*: Digital prescription creation
- 🚧 *Patient Communication*: Secure messaging system
- 📋 *Analytics Dashboard*: Patient statistics and health trends

### For System Administrators
- ✅ *User Management*: Control access and permissions
- 📋 *System Monitoring*: Application performance and usage analytics
- 📋 *Data Backup*: Automated backup and recovery systems
- 📋 *Compliance Reporting*: Generate regulatory compliance reports

---

## 🔐 Security Features

- *JWT Authentication*: Secure token-based authentication
- *Role-Based Access Control*: Different permissions for patients, doctors, and admins
- *Data Encryption*: All sensitive data encrypted at rest and in transit
- *Audit Logging*: Track all access to medical records
- *CORS Protection*: Restricted cross-origin requests
- *Input Validation*: Comprehensive sanitization of user inputs

---

## 📱 Mobile Responsiveness

TajiAfya is built with a mobile-first approach:
- *Responsive Design*: Optimized for all screen sizes
- *Touch-Friendly*: Large buttons and intuitive gestures
- *Offline Capability*: Core features available without internet (planned)
- *Progressive Web App*: Installable on mobile devices (planned)

---

## 🌍 Impact and Future Vision

### Target Demographics
- *Primary*: Patients with chronic conditions in underserved communities
- *Secondary*: Rural healthcare providers with limited resources
- *Tertiary*: Urban populations seeking convenient healthcare access

### Social Impact Goals
1. *Reduce Healthcare Inequality*: Bridge the gap in medical access
2. *Improve Health Outcomes*: Early detection and continuous monitoring
3. *Empower Patients*: Give individuals control over their health data
4. *Support Healthcare Workers*: Reduce administrative burden
5. *Data-Driven Healthcare*: Enable evidence-based medical decisions

### Expansion Roadmap
- *Phase 1*: Local community deployment
- *Phase 2*: Regional healthcare network integration
- *Phase 3*: Multi-language support for global reach
- *Phase 4*: AI-powered diagnostic assistance
- *Phase 5*: IoT device integration for automated health monitoring

---

## 🤝 Contributing

We welcome contributions to TajiAfya! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### Development Workflow
1. Fork the repository
2. Create a feature branch (git checkout -b feature/AmazingFeature)
3. Commit changes (git commit -m 'Add some AmazingFeature')
4. Push to branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Team

*Developer*: Patrick Nganga  
*Role*: Full-Stack Developer  
*Program*: PLP MERN Stack Development - Week 8 Capstone  

---

## 📞 Support

For support, please contact:
- *Email*: support@tajiafya.com
- *GitHub Issues*: [Report a bug](https://github.com/PLP-MERN-Stack-Development/week-8-capstone_-pat123456789g/issues)
- *Documentation*: [Wiki](https://github.com/PLP-MERN-Stack-Development/week-8-capstone_-pat123456789g/wiki)

---

## 🙏 Acknowledgments

- *PLP Academy* for the comprehensive MERN stack curriculum
- *Healthcare Professionals* who provided domain expertise
- *Open Source Community* for the amazing tools and libraries
- *Beta Users* who provided valuable feedback during development

---

"Empowering health, one digital interaction at a time." - TajiAfya Team

---

*Legend:*
- ✅ Completed
- 🚧 In Progress  
- 📋 Planned
- 🚀 Future Scope
