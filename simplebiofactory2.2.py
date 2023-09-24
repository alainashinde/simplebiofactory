import numpy as np
import pandas as pd

# Define constants
NUM_PATIENTS = 100  # Number of patients to simulate
NUM_GENES = 50  # Number of genes in the genetic data

# Create a list to store patient records
patient_records = []

# Function to generate detailed simulated patient data including genetics
def generate_patient_data():
    # Simulated health profile data (more parameters)
    patient_data = {
        'genetics': {
            'Gene1': np.random.rand(),  # Simulated genetic variation for Gene1
            'Gene2': np.random.rand(),  # Simulated genetic variation for Gene2
            # Add more genes and associated data here...
        },
        'medical_history': np.random.choice(['Allergy', 'Hypertension', 'Diabetes'], 2),  # Simulated medical history
        'current_health': np.random.choice(['Poor', 'Fair', 'Good'], 1)[0],  # Simulated current health status
    }
    return patient_data

# Function to simulate the AI-driven therapy selection for a patient considering genetics, medical history, and current health
def ai_workflow(patient_data):
    # Simulated AI algorithm for therapy selection based on multiple parameters
    selected_therapy = 'No specific recommendation'

    # Define the impact of genes on therapy selection
    gene_impact = {
        'Gene1': {
            'Hypertension': 'Prescription antihypertensive drug (Moderate genetic risk)',
            'Diabetes': 'Oral diabetes medication (Low genetic risk)',
            'Allergy': 'Allergy medication (antihistamine)',
        },
        'Gene2': {
            'Hypertension': 'Lifestyle modification for hypertension',
            'Diabetes': 'Insulin therapy (Moderate genetic risk)',
            'Allergy': 'Allergy medication (antihistamine)',
        },
        # Define impacts for more genes and conditions...
    }

    for condition in patient_data['medical_history']:
        gene = f'Gene{np.random.choice(list(range(1, NUM_GENES + 1)), 1)[0]}'  # Randomly select a gene

        # Check if the selected gene is in the dictionary, otherwise use a default therapy (temp until can add more)
        if gene in gene_impact:
            selected_therapy = gene_impact[gene][condition]
        else:
            selected_therapy = 'Default therapy for missing gene'

    return selected_therapy

# Function to simulate the biomanufacturing process for a therapy, including dosage adjustments
def biomanufacturing(selected_therapy, patient_data):
    # Simulated synthetic biology and bioreactor process based on therapy
    engineered_microorganism = None
    bioreactor_process = 'Bioreactor idle'
    dosage_adjustment = 'Standard dosage'

    if 'antihypertensive' in selected_therapy.lower():
        engineered_microorganism = 'Engineered microorganism for antihypertensive drug production'
        bioreactor_process = 'Bioreactor producing antihypertensive drug'

        # Simulate dosage adjustment based on genetics
        dosage_gene = 'Gene1'  # Gene responsible for dosage adjustments
        if patient_data['genetics'][dosage_gene] > 0.6:
            dosage_adjustment = 'Higher dosage (High genetic risk)'
        elif patient_data['genetics'][dosage_gene] > 0.3:
            dosage_adjustment = 'Moderate dosage (Moderate genetic risk)'

    elif 'Insulin therapy' in selected_therapy:
        engineered_microorganism = 'Engineered microorganism for insulin production'
        bioreactor_process = 'Bioreactor producing insulin'

        # Simulate dosage adjustment based on genetics
        dosage_gene = 'Gene2'  # Gene responsible for dosage adjustments
        if patient_data['genetics'][dosage_gene] > 0.6:
            dosage_adjustment = 'Higher insulin dosage (High genetic risk)'
        elif patient_data['genetics'][dosage_gene] > 0.3:
            dosage_adjustment = 'Moderate insulin dosage (Moderate genetic risk)'

    elif 'Oral diabetes medication' in selected_therapy:
        engineered_microorganism = 'Engineered microorganism for oral diabetes medication production'

    elif 'Allergy medication' in selected_therapy:
        engineered_microorganism = 'Engineered microorganism for allergy medication production'

    return engineered_microorganism, bioreactor_process, dosage_adjustment

# Simulate multiple patients and their workflows
for patient_id in range(1, NUM_PATIENTS + 1):
    print(f"Simulating Patient {patient_id}")
    patient_data = generate_patient_data()
    
    # Check if the outcome_gene exists in the patient's genetic data
    outcome_gene = 'Gene3'  # Gene responsible for therapy outcomes
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

    # Store patient record, therapy history, and outcome in the list
    patient_record = {
        'Patient_ID': patient_id,
        'Genetics': patient_data['genetics'],
        'Medical_History': patient_data['medical_history'],
        'Current_Health': patient_data['current_health'],
        'Selected_Therapy': selected_therapy,
        'Engineered_Microorganism': engineered_microorganism,
        'Bioreactor_Process': bioreactor_process,
        'Outcome': outcome,
    }
    
    patient_records.append(patient_record)  # Append the record to the list

# Create the patient database from the list of patient records
patient_database = pd.DataFrame(patient_records)

# Display patient database (not needed so commented out)
# print("\nPatient Database:")
# print(patient_database)

# After simulating all patients and creating the patient_records list
for patient_record in patient_records:
    patient_id = patient_record['Patient_ID']
    selected_therapy = patient_record['Selected_Therapy']
    engineered_microorganism = patient_record['Engineered_Microorganism']
    bioreactor_process = patient_record['Bioreactor_Process']
    outcome = patient_record['Outcome']

    print(f"Patient {patient_id} - Selected Therapy: {selected_therapy}")
    print(f"Patient {patient_id} - Engineered Microorganism: {engineered_microorganism}")
    print(f"Patient {patient_id} - Bioreactor Process: {bioreactor_process}")
    print(f"Patient {patient_id} - Outcome: {outcome}\n")
