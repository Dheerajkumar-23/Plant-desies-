"""Treatment and prevention advice for PlantVillage disease classes.

Matching is keyword based on the class folder name, so it works even if the
folder names differ slightly between dataset versions.
"""

DISCLAIMER = ("General guidance only. Confirm the diagnosis and check chemical "
              "labels and local rules with your agricultural extension officer.")

HEALTHY = {
    "about": "The leaf looks healthy.",
    "treatment": ["No treatment needed."],
    "prevention": ["Water at the base, keep good spacing and airflow, "
                   "and check plants weekly for early symptoms."],
}

FUNGAL_GENERIC = {
    "about": "Fungal or leaf disease detected.",
    "treatment": [
        "Remove and destroy badly infected leaves.",
        "Apply a suitable fungicide (for example copper-based or mancozeb) as per label.",
    ],
    "prevention": ["Avoid overhead watering.", "Rotate crops and clean up plant debris."],
}

# (keywords, info) - first match wins, so keep specific entries first.
RULES = [
    (["healthy"], HEALTHY),
    (["cedar"], {
        "about": "Cedar apple rust: orange-yellow spots caused by a fungus that alternates with juniper/cedar trees.",
        "treatment": ["Apply fungicide (myclobutanil or mancozeb) from pink bud stage through early summer.",
                      "Remove nearby galls on cedar/juniper if possible."],
        "prevention": ["Plant resistant apple varieties.", "Rake and destroy fallen leaves."]}),
    (["scab"], {
        "about": "Apple scab: olive-brown scabby spots on leaves and fruit caused by a fungus.",
        "treatment": ["Spray fungicide (captan, sulfur or myclobutanil) from green tip, repeating every 7-10 days in wet weather.",
                      "Remove infected leaves and fruit."],
        "prevention": ["Rake and destroy fallen leaves in autumn.", "Prune for airflow; choose resistant varieties."]}),
    (["black_rot", "black rot"], {
        "about": "Black rot: dark leaf spots and rotting fruit caused by a fungus.",
        "treatment": ["Prune out infected shoots, leaves and mummified fruit and destroy them.",
                      "Apply fungicide (captan, mancozeb or myclobutanil) as per label."],
        "prevention": ["Keep canopy open for airflow.", "Remove fallen debris and old fruit."]}),
    (["esca", "black_measles"], {
        "about": "Esca (black measles): a fungal trunk disease causing striped, scorched leaves.",
        "treatment": ["No full cure. Prune and burn affected wood during dry weather.",
                      "Protect pruning cuts with a wound sealant."],
        "prevention": ["Avoid large pruning wounds.", "Use clean, disinfected tools."]}),
    (["isariopsis"], {
        "about": "Grape leaf blight (Isariopsis leaf spot): dark angular spots on leaves.",
        "treatment": ["Remove affected leaves.", "Apply copper-based or mancozeb fungicide."],
        "prevention": ["Improve airflow and sunlight in the canopy.", "Clear fallen leaves."]}),
    (["powdery"], {
        "about": "Powdery mildew: white powdery coating on leaves.",
        "treatment": ["Spray sulfur, potassium bicarbonate, neem oil or a suitable fungicide.",
                      "Remove heavily infected leaves."],
        "prevention": ["Give plants space and sunlight.", "Avoid excess nitrogen fertilizer."]}),
    (["cercospora", "gray_leaf"], {
        "about": "Gray leaf spot: rectangular tan-gray lesions on corn leaves.",
        "treatment": ["Apply a foliar fungicide (strobilurin or triazole) if disease is early and spreading."],
        "prevention": ["Rotate crops and till residue.", "Plant resistant hybrids; avoid dense planting."]}),
    (["northern"], {
        "about": "Northern leaf blight: long cigar-shaped gray-green lesions on corn.",
        "treatment": ["Apply a foliar fungicide at early disease onset."],
        "prevention": ["Use resistant hybrids.", "Rotate crops and bury residue."]}),
    (["common_rust", "rust"], {
        "about": "Rust: small orange-brown pustules on leaves.",
        "treatment": ["Apply a fungicide (triazole or strobilurin) if infection is early and severe."],
        "prevention": ["Plant resistant varieties.", "Plant early to avoid peak rust season."]}),
    (["haunglongbing", "greening"], {
        "about": "Citrus greening (HLB): bacterial disease spread by psyllid insects. It has no cure.",
        "treatment": ["Remove and destroy infected trees to protect others.",
                      "Control psyllids with approved insecticides."],
        "prevention": ["Buy certified disease-free plants.", "Monitor and control psyllids regularly."]}),
    (["bacterial_spot", "bacterial spot"], {
        "about": "Bacterial spot: small dark water-soaked spots on leaves and fruit.",
        "treatment": ["Spray copper-based bactericide (often mixed with mancozeb).",
                      "Remove infected leaves; avoid working in wet plants."],
        "prevention": ["Use disease-free seed or plants.", "Water at the base; rotate crops."]}),
    (["early_blight"], {
        "about": "Early blight: brown spots with concentric rings, usually on older leaves.",
        "treatment": ["Remove infected lower leaves.", "Apply chlorothalonil, mancozeb or copper fungicide."],
        "prevention": ["Rotate crops (2-3 years).", "Mulch, stake plants and avoid overhead watering."]}),
    (["late_blight"], {
        "about": "Late blight: fast-spreading water-soaked lesions, can destroy a crop in days.",
        "treatment": ["Act immediately: remove and destroy infected plants.",
                      "Apply fungicide (chlorothalonil, mancozeb or copper); do not compost infected material."],
        "prevention": ["Use certified seed and resistant varieties.", "Avoid wet foliage; improve airflow."]}),
    (["leaf_scorch"], {
        "about": "Leaf scorch: purple-brown spots that merge, causing a scorched look.",
        "treatment": ["Remove infected leaves.", "Apply a suitable fungicide if severe."],
        "prevention": ["Avoid overhead watering.", "Space plants and renew old beds."]}),
    (["leaf_mold"], {
        "about": "Leaf mold: yellow spots on top and olive mold underneath, common in humid conditions.",
        "treatment": ["Reduce humidity and improve ventilation.", "Apply copper or chlorothalonil fungicide."],
        "prevention": ["Space plants and prune lower leaves.", "Water in the morning at the base."]}),
    (["septoria"], {
        "about": "Septoria leaf spot: many small circular spots with dark borders.",
        "treatment": ["Remove infected leaves.", "Apply chlorothalonil, mancozeb or copper fungicide."],
        "prevention": ["Rotate crops.", "Mulch to stop soil splash; avoid wetting leaves."]}),
    (["spider", "mite"], {
        "about": "Spider mites: tiny pests causing stippled, yellowing leaves and fine webbing.",
        "treatment": ["Spray plants with water to knock mites off.",
                      "Use insecticidal soap, neem oil or a miticide."],
        "prevention": ["Keep plants well watered (mites like dry, dusty conditions).", "Encourage natural predators."]}),
    (["target_spot"], {
        "about": "Target spot: brown lesions with ring patterns.",
        "treatment": ["Remove infected leaves.", "Apply chlorothalonil or mancozeb fungicide."],
        "prevention": ["Improve airflow; avoid overhead watering.", "Rotate crops."]}),
    (["yellow_leaf_curl", "curl_virus"], {
        "about": "Tomato yellow leaf curl virus: curled, yellow leaves spread by whiteflies. No cure.",
        "treatment": ["Remove and destroy infected plants.", "Control whiteflies (yellow sticky traps, neem oil, insecticide)."],
        "prevention": ["Use resistant varieties and insect netting.", "Control weeds around the field."]}),
    (["mosaic"], {
        "about": "Mosaic virus: mottled light/dark green leaves. No cure.",
        "treatment": ["Remove and destroy infected plants.", "Disinfect hands and tools."],
        "prevention": ["Use certified virus-free seed.", "Do not smoke or handle tobacco before touching plants."]}),
]


def get_advice(class_name):
    key = class_name.lower().replace(" ", "_")
    for keywords, info in RULES:
        if any(k in key for k in keywords):
            return info
    return FUNGAL_GENERIC
