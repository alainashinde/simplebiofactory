import numpy as np
import pandas as pd

# Define constants
NUM_PATIENTS = 1000  # Number of patients to simulate
NUM_GENES = 200  # Number of genes in the genetic data

# Create a database to store patient records and therapy history
patient_database = pd.DataFrame(columns=['Patient_ID', 'Genetics', 'Medical_History', 'Current_Health',
                                         'Selected_Therapy', 'Engineered_Microorganism', 'Bioreactor_Process', 'Dosage_Adjustment', 'Outcome'])

# Define genes with specific functions
GENES = {
    'Gene1': {'function': 'Drug Metabolism'},
    'Gene2': {'function': 'Hormone Regulation'},
    'Gene3': {'function': 'Immune Response'},
    # Add more genes with functions...
}

# Define therapy options and their genetic dependencies
THERAPIES = {
    'Antihypertensive': {
        'genes_required': ['Gene1'],
        'dosage_gene': 'Gene1',
        'dosage_levels': {
            'Low genetic risk': {'min': 0.0, 'max': 0.2},
            'Moderate genetic risk': {'min': 0.2, 'max': 0.7},
            'High genetic risk': {'min': 0.7, 'max': 1.0}
        },
        'bioreactor_process': 'Bioreactor producing antihypertensive drug',
    },
    'Insulin Therapy': {
        'genes_required': ['Gene2'],
        'dosage_gene': 'Gene2',
        'dosage_levels': {
            'Low genetic risk': {'min': 0.0, 'max': 0.2},
            'Moderate genetic risk': {'min': 0.2, 'max': 0.7},
            'High genetic risk': {'min': 0.7, 'max': 1.0}
        },
        'bioreactor_process': 'Bioreactor producing insulin',
    },
    'Oral Diabetes Medication': {
        'genes_required': [],
        'bioreactor_process': 'Bioreactor producing oral diabetes medication',
    },
    'Allergy Medication': {
        'genes_required': [],
        'bioreactor_process': 'Bioreactor producing allergy medication',
    },
    # Add more therapy options...
}

# Function to generate detailed simulated patient data including genetics
def generate_patient_data():
    # Simulated health profile data (more parameters)
    patient_data = {
        'genetics': {gene: np.random.rand() for gene in GENES},  # Simulated genetic variations for genes
        'medical_history': np.random.choice(['Allergy', 'Hypertension', 'Diabetes', 'Asthma', 'Cancer'], 2),  # Simulated medical history
        'current_health': np.random.choice(['Poor', 'Fair', 'Good'], 1)[0],  # Simulated current health status
    }
    return patient_data

# Function to simulate the AI-driven therapy selection for a patient considering genetics, medical history, and current health
def ai_workflow(patient_data):
    # Simulated AI algorithm for therapy selection based on multiple parameters
    selected_therapy = 'No specific recommendation'

    # Determine eligible therapies based on medical history
    eligible_therapies = [therapy for therapy in THERAPIES if set(THERAPIES[therapy]['genes_required']).issubset(patient_data['genetics'])]

    if eligible_therapies:
        # Prioritize therapies based on medical history
        for condition in patient_data['medical_history']:
            for therapy in eligible_therapies:
                if condition in THERAPIES[therapy]['genes_required']:
                    selected_therapy = therapy
                    break

    return selected_therapy

# Function to simulate the biomanufacturing process for a therapy, including dosage adjustments
def biomanufacturing(selected_therapy, patient_data):
    # Simulated synthetic biology and bioreactor process based on therapy
    engineered_microorganism = None
    bioreactor_process = 'Bioreactor idle'
    dosage_adjustment = 'Standard dosage'

    if selected_therapy in THERAPIES:
        therapy_info = THERAPIES[selected_therapy]

        if 'bioreactor_process' in therapy_info:
            engineered_microorganism = f'Engineered microorganism for {selected_therapy} production'
            bioreactor_process = therapy_info['bioreactor_process']

            # Simulate dosage adjustment based on genetics
            dosage_gene = therapy_info['dosage_gene']
            if dosage_gene:
                dosage_range = therapy_info['dosage_levels']
                genetic_value = patient_data['genetics'][dosage_gene]
                for level, level_range in dosage_range.items():
                    if level_range['min'] <= genetic_value <= level_range['max']:
                        dosage_adjustment = level
                        break

    return engineered_microorganism, bioreactor_process, dosage_adjustment

# Simulate multiple patients and their workflows
patient_records = []  # Create a list to store patient records

for patient_id in range(1, NUM_PATIENTS + 1):
    print(f"Simulating Patient {patient_id}")
    patient_data = generate_patient_data()

    selected_therapy = ai_workflow(patient_data)
    engineered_microorganism, bioreactor_process, dosage_adjustment = biomanufacturing(selected_therapy, patient_data)

    # Simulate therapy outcomes
    outcome_gene = np.random.choice(list(GENES.keys()))
    outcome = 'No outcome data available'
    if outcome_gene in patient_data['genetics']:
        genetic_value = patient_data['genetics'][outcome_gene]
        if 0.7 <= genetic_value <= 1.0:
            outcome = 'Favorable outcome (High genetic risk)'
        elif 0.3 <= genetic_value < 0.7:
            outcome = 'Moderate outcome (Moderate genetic risk)'
        elif 0.0 <= genetic_value < 0.3:
            outcome = 'Standard outcome (Low genetic risk)'

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

# Create a DataFrame to store patient records
patient_database = pd.DataFrame(patient_records)

# Display patient database
#print("\nPatient Database:")
#print(patient_database)

# Iterate through the patient database and print results
for index, patient in patient_database.iterrows():
    print(f"Patient ID: {int(patient['Patient_ID'])}")
    print("Genetics:")
    for gene, value in patient['Genetics'].items():
        print(f"  {gene}: {value:.2f}")
    print(f"Medical History: {', '.join(patient['Medical_History'])}")
    print(f"Current Health: {patient['Current_Health']}")
    print(f"Selected Therapy: {patient['Selected_Therapy']}")

    # Display engineered microorganism and bioreactor process if applicable
    if patient['Engineered_Microorganism'] and patient['Bioreactor_Process']:
        print(f"Engineered Microorganism: {patient['Engineered_Microorganism']}")
        print(f"Bioreactor Process: {patient['Bioreactor_Process']}")

    # Display dosage adjustment if applicable
    if patient['Dosage_Adjustment']:
        print(f"Dosage Adjustment: {patient['Dosage_Adjustment']}")

    print(f"Outcome: {patient['Outcome']}")
    print("\n" + "-" * 50 + "\n")