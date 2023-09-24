import numpy as np
import pandas as pd

# Define constants
NUM_PATIENTS = 100  # Number of patients to simulate
NUM_GENES = 50  # Number of genes in the genetic data
NUM_MEDICAL_HISTORY_CONDITIONS = 30  # Number of possible medical history conditions

# Create a database to store patient records and therapy history
patient_database = pd.DataFrame(columns=['Patient_ID', 'Genetics', 'Medical_History', 'Current_Health',
                                         'Selected_Therapy', 'Engineered_Microorganism', 'Bioreactor_Process', 'Dosage_Adjustment', 'Outcome'])

# Function to generate detailed simulated patient data including genetics
def generate_patient_data():
    # Simulated health profile data (more parameters)
    patient_data = {
        'genetics': {
            'BRCA1': np.random.rand(),  # Simulated genetic variation for BRCA1
            'BRCA2': np.random.rand(),  # Simulated genetic variation for BRCA2
            'TP53': np.random.rand(),   # Simulated genetic variation for TP53
            'EGFR': np.random.rand(),   # Simulated genetic variation for EGFR
            'KRAS': np.random.rand(),   # Simulated genetic variation for KRAS
            # Add more genes and associated data here...
        },
        'medical_history': np.random.choice([
            'Allergy', 'Hypertension', 'Diabetes', 'Asthma', 'Depression', 'Arthritis', 'COPD', 'Obesity',
            'Hyperthyroidism', 'Migraine', 'Osteoporosis', 'Alzheimer\'s', 'Parkinson\'s', 'Schizophrenia',
            'Bipolar Disorder', 'Epilepsy', 'Multiple Sclerosis', 'Crohn\'s Disease', 'Ulcerative Colitis',
            'Rheumatoid Arthritis', 'Fibromyalgia', 'Celiac Disease', 'Lupus', 'Psoriasis', 'Endometriosis',
            'PCOS', 'Sickle Cell Anemia', 'HIV/AIDS',
            # Add more conditions here...
        ], NUM_MEDICAL_HISTORY_CONDITIONS),  # Simulated medical history
        'current_health': np.random.choice(['Poor', 'Fair', 'Good'], 1)[0],  # Simulated current health status
    }
    return patient_data

# Define the impact of genes on therapy selection
gene_impact = {
    'BRCA1': {
        'Cancer': 'Prophylactic surgery (High genetic risk)',
    },
    'BRCA2': {
        'Cancer': 'Prophylactic surgery (High genetic risk)',
    },
    'TP53': {
        'Cancer': 'Aggressive treatment and monitoring (High genetic risk)',
    },
    'EGFR': {
        'Lung Cancer': 'EGFR inhibitor therapy (Specific genetic mutation)',
    },
    'KRAS': {
        'Lung Cancer': 'Immunotherapy (Specific genetic mutation)',
    },
    # Continue defining impacts for more genes and conditions...
}

# Function to simulate the AI-driven therapy selection for a patient considering genetics, medical history, and current health
def ai_workflow(patient_data):
    # Simulated AI algorithm for therapy selection based on multiple parameters
    selected_therapy = 'No specific recommendation'

    for condition in patient_data['medical_history']:
        gene = np.random.choice(list(patient_data['genetics'].keys()), 1)[0]  # Randomly select a gene

        # Check if the selected gene is in the dictionary, otherwise use a default therapy
        if gene in gene_impact:
            selected_therapy = gene_impact[gene].get(condition, 'Default therapy for missing gene')

    return selected_therapy

# Function to simulate the biomanufacturing process for a therapy, including dosage adjustments
def biomanufacturing(selected_therapy, patient_data):
    # Simulated synthetic biology and bioreactor process based on therapy
    engineered_microorganism = None
    bioreactor_process = 'Bioreactor idle'
    dosage_adjustment = 'Standard dosage'

    if 'surgery' in selected_therapy.lower():
        engineered_microorganism = 'No engineered microorganism needed'
        bioreactor_process = 'No bioreactor needed'
        dosage_adjustment = 'No dosage adjustment needed'

    elif 'EGFR inhibitor therapy' in selected_therapy:
        engineered_microorganism = 'Engineered microorganism for EGFR inhibitor production'
        bioreactor_process = 'Bioreactor producing EGFR inhibitor'

        # Simulate dosage adjustment based on genetics
        dosage_gene = 'EGFR'  # Gene responsible for dosage adjustments
        if patient_data['genetics'][dosage_gene] > 0.6:
            dosage_adjustment = 'Higher dosage (High genetic risk)'
        elif patient_data['genetics'][dosage_gene] > 0.3:
            dosage_adjustment = 'Moderate dosage (Moderate genetic risk)'

    # Continue to define biomanufacturing for other therapies and genes...

    return engineered_microorganism, bioreactor_process, dosage_adjustment

# Simulate multiple patients and their workflows
patient_records = []  # Create a list to store patient records

for patient_id in range(1, NUM_PATIENTS + 1):
    print(f"Simulating Patient {patient_id}")
    patient_data = generate_patient_data()
    
    # Check if the outcome_gene exists in the patient's genetic data
    outcome_gene = 'EGFR'  # Gene responsible for therapy outcomes
    if outcome_gene in patient_data['genetics']:
        if patient_data['genetics'][outcome_gene] > 0.6:
            outcome = 'Favorable outcome (High genetic risk)'
        elif patient_data['genetics'][outcome_gene] > 0.3:
            outcome = 'Moderate outcome (Moderate genetic risk)'
        else:
            outcome = 'Standard outcome (Low genetic risk)'
    else:
        outcome = 'Gene not found in genetic data'

    selected_therapy = ai_workflow(patient_data)
    engineered_microorganism, bioreactor_process, dosage_adjustment = biomanufacturing(selected_therapy, patient_data)

    # Store patient record, therapy history, and outcome in the database
    patient_record = {
        'Patient_ID': patient_id,
        'Genetics': patient_data['genetics'],
        'Medical_History': patient_data['medical_history'],
        'Current_Health': patient_data['current_health'],
        'Selected_Therapy': selected_therapy,
        'Engineered_Microorganism': engineered_microorganism,
        'Bioreactor_Process': bioreactor_process,
        'Dosage_Adjustment': dosage_adjustment,
        'Outcome': outcome,
    }
    patient_records.append(patient_record)

# Convert the list of patient records to a DataFrame
patient_database = pd.DataFrame(patient_records)

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)  # Display all rows
pd.set_option('display.max_columns', None)  # Display all columns

# Display patient database
print("\nPatient Database:")
print(patient_database)
