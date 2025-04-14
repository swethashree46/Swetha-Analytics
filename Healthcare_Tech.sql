CREATE DATABASE healthcare_tech_db;
USE healthcare_tech_db;

CREATE TABLE technology (
    tech_id INT PRIMARY KEY,
    tech_name VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    
    success_status VARCHAR(20), -- Values: 'Success' or 'Failure'
    status VARCHAR(20),         -- Values: 'In Progress', 'Completed', 'Aborted'
    
    impact_area VARCHAR(100),   -- e.g., 'Patient Care', 'Diagnostics', etc.
    cost_category VARCHAR(100), -- e.g., 'High', 'Medium', 'Low'
    
    manpower_change VARCHAR(20),      -- Values: 'Increased' or 'Decreased'
    employment_impact VARCHAR(20),    -- Values: 'Increased' or 'Decreased'
    
    reason_over_tradition VARCHAR(100),  -- e.g., 'Time-saving', 'Remote access'
    advantages VARCHAR(100),             -- e.g., 'Cost-effective', 'Speed'
    disadvantages VARCHAR(100),          -- e.g., 'Privacy issues', 'High cost'
    
    current_stage VARCHAR(100),     -- e.g., 'Prototype', 'Implemented', etc.
    description TEXT,
    source_link TEXT
);

INSERT INTO technology (
    tech_id, tech_name, year, success_status, status, impact_area, cost_category,
    manpower_change, employment_impact, reason_over_tradition, advantages, disadvantages,
    current_stage, description, source_link
) VALUES
(1, 'Telehealth', 2023, 'Success', 'Completed', 'Patient Care', 'Medium', 'Decreased', 'Increased', 'Remote access', 'Accessibility', 'Requires internet', 'Widely used', 'Virtual consultations and monitoring systems', 'https://www.rxnt.com/8-emerging-trends-in-healthcare-technology-for-2025'),

(2, 'AI in Diagnostics', 2024, 'Success', 'In Progress', 'Diagnostics', 'High', 'Decreased', 'Increased', 'Accuracy', 'Precision', 'High cost', 'Early adoption', 'AI helps analyze scans and lab results', 'https://www.theguardian.com/business/2025/mar/04/doctors-ai-healthcare'),

(3, 'Wearable Health Devices', 2025, 'Success', 'In Progress', 'Monitoring', 'Medium', 'Decreased', 'Increased', 'Continuous monitoring', 'Self-care', 'Battery issues', 'Adopting rapidly', 'Smartwatches track vitals and send alerts', 'https://www.medparkhospital.com/en-US/lifestyles/10-health-trends-of-2025'),

(4, 'Blockchain for Health Data', 2025, 'In Progress', 'In Progress', 'Data Security', 'High', 'Decreased', 'Decreased', 'Data integrity', 'Security', 'Complex to implement', 'Pilot phase', 'Secure storage of health records', 'https://www.theguardian.com/technology/2024/nov/22/healthcare-blockchain'),

(5, '3D Printing for Prosthetics', 2024, 'Success', 'Completed', 'Surgery', 'Medium', 'Decreased', 'Increased', 'Customization', 'Low cost', 'Limited reach', 'Mainstream use', 'Custom prosthetics at lower cost', 'https://www.statnews.com/2024/06/19/3d-printing-prosthetics-healthcare-tech'),

(6, 'Remote Patient Monitoring (RPM)', 2025, 'Success', 'In Progress', 'Monitoring', 'Medium', 'Decreased', 'Increased', 'Home care', 'Real-time alerts', 'Patient compliance needed', 'Partially implemented', 'Track chronic conditions remotely', 'https://www.rxnt.com/8-emerging-trends-in-healthcare-technology-for-2025'),

(7, 'Genomic Medicine', 2025, 'In Progress', 'In Progress', 'Diagnostics', 'High', 'Increased', 'Increased', 'Personalized treatment', 'Precision', 'Expensive testing', 'Growing interest', 'Treatment tailored to DNA', 'https://www.genomeweb.com/'),

(8, 'Nanomedicine', 2024, 'In Progress', 'In Progress', 'Treatment Delivery', 'High', 'Increased', 'Increased', 'Targeted therapy', 'Less side effects', 'Toxicity concerns', 'Research stage', 'Nanoparticles deliver drugs', 'https://www.sciencedaily.com/releases/2024/03/240305124204.htm'),

(9, 'AI Virtual Health Assistants', 2024, 'Success', 'Completed', 'Admin Automation', 'Medium', 'Decreased', 'Decreased', 'Efficiency', 'Availability', 'Trust issues', 'Early use in hospitals', '24/7 digital patient interaction', 'https://www.mobihealthnews.com/2024/02/ai-powered-virtual-health-assistants'),

(10, 'Robotic Surgery', 2023, 'Success', 'Completed', 'Surgery', 'High', 'Increased', 'Increased', 'Precision', 'Minimal invasion', 'Training required', 'Fully used', 'Robots aid surgeons in critical surgeries', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7041022/'),

(11, 'EHR Systems', 2024, 'Success', 'Completed', 'Data Management', 'High', 'Decreased', 'Increased', 'Digital records', 'Speed', 'Cyber risks', 'Global use', 'Electronic Health Records for fast access', 'https://www.healthit.gov/topic/scientific-initiatives/advancing-health-it'),

(12, 'Augmented Reality (AR) in Surgery', 2023, 'Success', 'In Progress', 'Surgery', 'High', 'Increased', 'Increased', 'Visual aid', 'Accuracy', 'Costly hardware', 'Testing in hospitals', '3D overlay for surgical navigation', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7076940/'),

(13, 'Precision Medicine', 2024, 'Success', 'In Progress', 'Treatment Delivery', 'High', 'Increased', 'Increased', 'Personalization', 'Effectiveness', 'Expensive', 'Used in oncology', 'Genetic-based personalized care', 'https://www.nature.com/articles/d41586-020-00194-8'),

(14, 'Mobile Health Apps', 2024, 'Success', 'Completed', 'Monitoring', 'Low', 'Decreased', 'Increased', 'Accessibility', 'Self-monitoring', 'Privacy issues', 'Mainstream', 'Health apps for fitness and care', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7476704/'),

(15, 'Smart Hospitals', 2025, 'In Progress', 'In Progress', 'Infrastructure', 'High', 'Decreased', 'Increased', 'Automation', 'Efficiency', 'Expensive setup', 'Emerging trend', 'IoT and AI in hospital management', 'https://www.forbes.com/healthcare-trends/'),

(16, 'AI-Assisted Surgery', 2025, 'Success', 'In Progress', 'Surgery', 'High', 'Increased', 'Increased', 'Reduced error', 'Precision', 'Setup cost', 'Expanding', 'AI-supported surgical procedures', 'https://www.bbc.com/news/health-45758634'),

(17, 'Chatbots for Mental Health', 2023, 'Success', 'Completed', 'Mental Health', 'Low', 'Decreased', 'Increased', 'Anonymous help', 'Access', 'Limited capability', 'Widely used', 'Bots offering basic mental care support', 'https://www.psychologytoday.com/us/therapy/types/online-therapy'),

(18, 'Cloud Healthcare Systems', 2025, 'Success', 'Completed', 'Data Management', 'Medium', 'Decreased', 'Increased', 'Remote access', 'Collaboration', 'Data breach risks', 'Standardized', 'Cloud storage for health data', 'https://www.healthcareitnews.com/news/cloud-computing-healthcare-growing-rapidly'),

(19, 'AI for Drug Discovery', 2024, 'In Progress', 'In Progress', 'Pharmaceuticals', 'High', 'Decreased', 'Increased', 'Faster research', 'Speed', 'Validation required', 'Pilot stage', 'AI to accelerate molecule discovery', 'https://www.nature.com/articles/s41587-020-0548-6'),

(20, 'Digital Pathology', 2024, 'Success', 'Completed', 'Diagnostics', 'Medium', 'Decreased', 'Increased', 'Faster diagnosis', 'Clarity', 'High resolution needed', 'Adopted by labs', 'Scanning slides and AI interpretation', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7060544/'),

(21, 'Cybersecurity Solutions', 2024, 'Success', 'Completed', 'Data Security', 'Medium', 'Increased', 'Increased', 'Data protection', 'Security', 'Implementation cost', 'Growing demand', 'Preventing healthcare data breaches', 'https://www.healthit.gov/topic/cybersecurity'),

(22, 'AI Radiology Assist', 2023, 'Success', 'Completed', 'Diagnostics', 'Medium', 'Decreased', 'Increased', 'Image reading', 'Speed', 'Mistrust', 'Integrated in tools', 'AI helps radiologists in scan analysis', 'https://pubmed.ncbi.nlm.nih.gov/'),

(23, 'Home ICU Monitoring', 2024, 'Success', 'In Progress', 'Monitoring', 'High', 'Decreased', 'Increased', 'Convenience', 'Remote alerts', 'Tech dependency', 'Expanding', 'ICU-grade care at home', 'https://www.ncbi.nlm.nih.gov/'),

(24, 'Bio-sensors', 2023, 'In Progress', 'In Progress', 'Diagnostics', 'Medium', 'Increased', 'Increased', 'Real-time detection', 'Sensitivity', 'Costly', 'Under testing', 'Sensors for glucose, oxygen, and more', 'https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/biosensor'),

(25, 'Voice Recognition EHR', 2024, 'Success', 'Completed', 'Admin Automation', 'Low', 'Decreased', 'Decreased', 'Hands-free use', 'Speed', 'Accent issues', 'Widely used', 'Doctors dictate notes directly to system', 'https://www.healthit.gov'),

(26, 'AI-Powered Triage', 2025, 'Success', 'Completed', 'Patient Care', 'Low', 'Decreased', 'Decreased', 'Quick assessment', 'Speed', 'Misjudgment risk', 'ERs adopting', 'AI assigns urgency in emergency', 'https://www.ncbi.nlm.nih.gov'),

(27, 'Digital Therapeutics', 2024, 'In Progress', 'In Progress', 'Mental Health', 'Low', 'Decreased', 'Increased', 'Remote treatment', 'Supportive care', 'Less regulation', 'Used in apps', 'Apps providing CBT, mindfulness tools', 'https://www.digitalmedicine.org'),

(28, 'Electronic Prescriptions (eRx)', 2023, 'Success', 'Completed', 'Admin Automation', 'Low', 'Decreased', 'Decreased', 'Paperless', 'Speed', 'Requires training', 'Fully rolled out', 'Doctors send scripts to pharmacies electronically', 'https://www.ncbi.nlm.nih.gov'),

(29, 'AI-Based ICU Management', 2025, 'In Progress', 'In Progress', 'Infrastructure', 'High', 'Decreased', 'Increased', 'Automation', 'Resource use', 'Needs training', 'Pilot in progress', 'AI manages ICU beds, alarms, resources', 'https://www.healthcareitnews.com'),

(30, 'Smart Ambulances', 2025, 'Success', 'Completed', 'Emergency Care', 'High', 'Decreased', 'Increased', 'Quick response', 'Life saving', 'Connectivity issues', 'In operation', 'Ambulances with real-time vitals & communication', 'https://www.ncbi.nlm.nih.gov');


