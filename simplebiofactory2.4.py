import numpy as np
import pandas as pd

# Define constants
NUM_PATIENTS = 100  # Number of patients to simulate
NUM_GENES = 50  # Number of genes in the genetic data

# Create a database to store patient records and therapy history
patient_database = pd.DataFrame(columns=['Patient_ID', 'Genetics', 'Medical_History', 'Current_Health',
                                         'Selected_Therapy', 'Engineered_Microorganism', 'Bioreactor_Process', 'Dosage_Adjustment', 'Outcome'])

# Function to generate detailed simulated patient data including genetics
def generate_patient_data():
    # Simulated health profile data
    patient_data = {
        'genetics': {
            'BRCA1': np.random.rand(),  # Simulated genetic variation for BRCA1
            'APOE': np.random.rand(),  # Simulated genetic variation for APOE
            'TP53': np.random.rand(),  # Simulated genetic variation for TP53
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
        'BRCA1': {
            'Hypertension': 'Prescription antihypertensive drug (Moderate genetic risk)',
            'Diabetes': 'Oral diabetes medication (Low genetic risk)',
            'Allergy': 'Allergy medication (antihistamine)',
        },
        'APOE': {
            'Hypertension': 'Lifestyle modification for hypertension',
            'Diabetes': 'Insulin therapy (Moderate genetic risk)',
            'Allergy': 'Allergy medication (antihistamine)',
        },
        'TP53': {
            'Hypertension': 'Prescription antihypertensive drug (Low genetic risk)',
            'Diabetes': 'Oral diabetes medication (High genetic risk)',
            'Allergy': 'Allergy medication (Moderate genetic risk)',
        },
        # Define impacts for more genes and conditions...
    }

    for condition in patient_data['medical_history']:
        gene = np.random.choice(list(patient_data['genetics'].keys()), 1)[0]  # Randomly select a gene

        # Check if the selected gene is in the dictionary, otherwise use a default therapy
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
        dosage_gene = 'BRCA1'  # Gene responsible for dosage adjustments
        if patient_data['genetics'][dosage_gene] > 0.6:
            dosage_adjustment = 'Higher dosage (High genetic risk)'
        elif patient_data['genetics'][dosage_gene] > 0.3:
            dosage_adjustment = 'Moderate dosage (Moderate genetic risk)'

    elif 'Insulin therapy' in selected_therapy:
        engineered_microorganism = 'Engineered microorganism for insulin production'
        bioreactor_process = 'Bioreactor producing insulin'

        # Simulate dosage adjustment based on genetics
        dosage_gene = 'APOE'  # Gene responsible for dosage adjustments
        if patient_data['genetics'][dosage_gene] > 0.6:
            dosage_adjustment = 'Higher insulin dosage (High genetic risk)'
        elif patient_data['genetics'][dosage_gene] > 0.3:
            dosage_adjustment = 'Moderate insulin dosage (Moderate genetic risk)'

    elif 'Oral diabetes medication' in selected_therapy:
        engineered_microorganism = 'Engineered microorganism for oral diabetes medication production'

    elif 'Allergy medication' in selected_therapy:
        engineered_microorganism = 'Engineered microorganism for allergy medication production'
        
        # Simulate drug blockers based on genetics
        drug_blocker_gene = 'TP53'  # Gene responsible for drug blockers
        if patient_data['genetics'][drug_blocker_gene] > 0.6:
            selected_therapy = 'Allergy medication (High genetic risk) - Drug blocked'
        elif patient_data['genetics'][drug_blocker_gene] > 0.3:
            selected_therapy = 'Allergy medication (Moderate genetic risk) - Drug partially blocked'

    return engineered_microorganism, bioreactor_process, dosage_adjustment, selected_therapy

# Simulate multiple patients and their workflows
for patient_id in range(1, NUM_PATIENTS + 1):
    print(f"Simulating Patient {patient_id}")
    patient_data = generate_patient_data()
    
    # Check if the outcome_gene exists in the patient's genetic data
    outcome_gene = 'BRCA1'  # Gene responsible for therapy outcomes
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
    engineered_microorganism, bioreactor_process, dosage_adjustment, selected_therapy = biomanufacturing(selected_therapy, patient_data)

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
    patient_database = patient_database.append(patient_record, ignore_index=True)

# Display patient database
print("\nPatient Database:")
print(patient_database)

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
