# Short disease info (Option A) — concise points for each of the 38 classes
# Keys must match exactly the class names in your class_indices.json

disease_details = {
 "Apple___Apple_scab": {
  "display_name": "Apple — Apple scab",
  "symptoms": ["Dark scabby spots on leaves", "Scabby lesions on fruit", "Leaf distortion/early drop"],
  "causes": ["Fungal pathogen (Venturia inaequalis)", "Favored by cool, wet weather"],
  "remedies": ["Remove infected leaves/fruit", "Apply recommended fungicide", "Prune to improve airflow"],
  "prevention": ["Use resistant varieties", "Avoid overhead watering", "Sanitation of fallen leaves"]
 },
 "Apple___Black_rot": {
  "display_name": "Apple — Black rot",
  "symptoms": ["Circular brown/black lesions on fruit", "Leaf spots with light centers", "Twig cankers"],
  "causes": ["Fungal pathogen (Botryosphaeria)", "Overwinters in mummified fruit"],
  "remedies": ["Remove mummified fruit", "Prune infected wood", "Use fungicides when needed"],
  "prevention": ["Sanitation", "Resistant cultivars", "Regular monitoring"]
 },
 "Apple___Cedar_apple_rust": {
  "display_name": "Apple — Cedar-apple rust",
  "symptoms": ["Yellow/orange leaf spots", "Orange gelatinous spore horns on junipers", "Premature leaf drop"],
  "causes": ["Gymnosporangium fungus", "Requires cedar/juniper alternate host"],
  "remedies": ["Remove nearby junipers if possible", "Apply protective fungicide", "Prune infected tissue"],
  "prevention": ["Avoid planting near junipers", "Use resistant varieties", "Monitor in spring"]
 },
 "Apple___healthy": {
  "display_name": "Apple — Healthy",
  "symptoms": ["No visible lesions", "Normal leaf color"],
  "causes": ["Healthy plant"],
  "remedies": ["No action required"],
  "prevention": ["Regular care and scouting"]
 },
 "Blueberry___healthy": {
  "display_name": "Blueberry — Healthy",
  "symptoms": ["Green leaves", "Normal fruiting"],
  "causes": ["Healthy plant"],
  "remedies": ["None"],
  "prevention": ["Maintain pH and drainage"]
 },
 "Cherry_(including_sour)___Powdery_mildew": {
  "display_name": "Cherry — Powdery mildew",
  "symptoms": ["White powdery coating on leaves", "Leaf curling", "Reduced vigor"],
  "causes": ["Powdery mildew fungus", "High humidity/shade"],
  "remedies": ["Apply sulfur or fungicide", "Prune for airflow", "Remove infected tissue"],
  "prevention": ["Plant in sun", "Avoid overhead watering"]
 },
 "Cherry_(including_sour)___healthy": {
  "display_name": "Cherry — Healthy",
  "symptoms": ["No visible disease"],
  "causes": ["Healthy plant"],
  "remedies": ["None"],
  "prevention": ["Routine care"]
 },
 "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
  "display_name": "Corn — Gray leaf spot",
  "symptoms": ["Rectangular tan lesions", "Lesions follow veins", "Reduced leaf area"],
  "causes": ["Cercospora fungus", "Warm, humid conditions"],
  "remedies": ["Crop rotation", "Fungicide when justified", "Residue management"],
  "prevention": ["Resistant hybrids", "Good drainage"]
 },
 "Corn_(maize)___Common_rust_": {
  "display_name": "Corn — Common rust",
  "symptoms": ["Reddish-brown pustules", "Leaf yellowing"],
  "causes": ["Puccinia rust fungus", "Spread by wind"],
  "remedies": ["Resistant varieties", "Fungicide if severe"],
  "prevention": ["Monitor fields", "Plant resistant hybrids"]
 },
 "Corn_(maize)___Northern_Leaf_Blight": {
  "display_name": "Corn — Northern leaf blight",
  "symptoms": ["Cigar-shaped lesions", "Lesion coalescence"],
  "causes": ["Exserohilum turcicum fungus", "Cool, moist weather"],
  "remedies": ["Resistant hybrids", "Fungicide in high pressure"],
  "prevention": ["Rotate crops", "Residue management"]
 },
 "Corn_(maize)___healthy": {
  "display_name": "Corn — Healthy",
  "symptoms": ["Uniform green leaves"],
  "causes": ["Healthy plant"],
  "remedies": ["None"],
  "prevention": ["Standard agronomy"]
 },
 "Grape___Black_rot": {
  "display_name": "Grape — Black rot",
  "symptoms": ["Brown leaf spots", "Shriveled black berries (mummies)"],
  "causes": ["Guignardia fungus", "Wet warm weather"],
  "remedies": ["Remove mummies", "Fungicide sprays", "Prune infected parts"],
  "prevention": ["Sanitation", "Canopy management"]
 },
 "Grape___Esca_(Black_Measles)": {
  "display_name": "Grape — Esca (Black measles)",
  "symptoms": ["Leaf striping", "Berry spotting", "Vine decline"],
  "causes": ["Wood-inhabiting fungi complex"],
  "remedies": ["Remove infected wood", "Improve vine health"],
  "prevention": ["Sanitation", "Avoid excessive wounding"]
 },
 "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
  "display_name": "Grape — Leaf blight",
  "symptoms": ["Irregular brown spots", "Leaf drop"],
  "causes": ["Isariopsis fungus", "Humid conditions"],
  "remedies": ["Copper sprays", "Remove diseased leaves"],
  "prevention": ["Canopy ventilation", "Avoid overcrowding"]
 },
 "Grape___healthy": {
  "display_name": "Grape — Healthy",
  "symptoms": ["Green leaves", "Normal bunch development"],
  "causes": ["Healthy plant"],
  "remedies": ["None"],
  "prevention": ["Routine monitoring"]
 },
 "Orange___Haunglongbing_(Citrus_greening)": {
  "display_name": "Orange — Citrus greening (HLB)",
  "symptoms": ["Yellow mottling on leaves", "Small misshapen fruit", "Decline"],
  "causes": ["Candidatus Liberibacter bacteria via psyllids"],
  "remedies": ["Remove infected trees", "Control psyllids with insecticides"],
  "prevention": ["Use certified disease-free stock", "Monitor and control psyllids"]
 },
 "Peach___Bacterial_spot": {
  "display_name": "Peach — Bacterial spot",
  "symptoms": ["Small dark spots on leaves", "Shot-hole fruit damage"],
  "causes": ["Xanthomonas bacteria", "Rain splash spread"],
  "remedies": ["Copper sprays", "Remove infected fruit"],
  "prevention": ["Sanitation", "Resistant varieties"]
 },
 "Peach___healthy": {
  "display_name": "Peach — Healthy",
  "symptoms": ["Healthy foliage and fruit"],
  "causes": ["Healthy plant"],
  "remedies": ["None"],
  "prevention": ["Regular care"]
 },
 "Pepper,_bell___Bacterial_spot": {
  "display_name": "Pepper — Bacterial spot",
  "symptoms": ["Water-soaked leaf spots", "Dark fruit lesions"],
  "causes": ["Bacterial pathogen", "Contaminated tools/seeds"],
  "remedies": ["Copper sprays", "Remove infected plants"],
  "prevention": ["Use clean seed", "Sanitize tools"]
 },
 "Pepper,_bell___healthy": {
  "display_name": "Pepper — Healthy",
  "symptoms": ["Green leaves", "No spots"],
  "causes": ["Healthy plant"],
  "remedies": ["None"],
  "prevention": ["Good cultural practice"]
 },
 "Potato___Early_blight": {
  "display_name": "Potato — Early blight",
  "symptoms": ["Concentric ring spots on leaves", "Leaf yellowing"],
  "causes": ["Alternaria solani fungus", "Older leaves commonly affected"],
  "remedies": ["Remove infected foliage", "Fungicide sprays"],
  "prevention": ["Rotate crops", "Mulch to reduce splash"]
 },
 "Potato___Late_blight": {
  "display_name": "Potato — Late blight",
  "symptoms": ["Water-soaked lesions", "White sporulation under humidity"],
  "causes": ["Phytophthora infestans", "Cool, humid conditions"],
  "remedies": ["Destroy infected plants", "Use recommended fungicides"],
  "prevention": ["Use certified seed", "Avoid excess moisture"]
 },
 "Potato___healthy": {
  "display_name": "Potato — Healthy",
  "symptoms": ["Green healthy foliage"],
  "causes": ["Healthy plant"],
  "remedies": ["None"],
  "prevention": ["Balanced nutrition"]
 },
 "Raspberry___healthy": {
  "display_name": "Raspberry — Healthy",
  "symptoms": ["Healthy leaves", "Normal canes"],
  "causes": ["Healthy plant"],
  "remedies": ["None"],
  "prevention": ["Proper pruning"]
 },
 "Soybean___healthy": {
  "display_name": "Soybean — Healthy",
  "symptoms": ["Green leaves", "Normal pods"],
  "causes": ["Healthy plant"],
  "remedies": ["None"],
  "prevention": ["Field scouting"]
 },
 "Squash___Powdery_mildew": {
  "display_name": "Squash — Powdery mildew",
  "symptoms": ["White powdery patches on leaves", "Leaf yellowing and curling"],
  "causes": ["Powdery mildew fungus", "Warm days and cool nights"],
  "remedies": ["Remove infected leaves", "Apply sulfur or potassium bicarbonate"],
  "prevention": ["Plant resistant varieties", "Improve airflow"]
 },
 "Strawberry___Leaf_scorch": {
  "display_name": "Strawberry — Leaf scorch",
  "symptoms": ["Brown/purple leaf spots", "Burned edges"],
  "causes": ["Fungal pathogen", "Moist conditions"],
  "remedies": ["Remove infected tissue", "Fungicide sprays"],
  "prevention": ["Avoid overhead watering", "Good spacing"]
 },
 "Strawberry___healthy": {
  "display_name": "Strawberry — Healthy",
  "symptoms": ["Green leaves", "Normal fruiting"],
  "causes": ["Healthy plant"],
  "remedies": ["None"],
  "prevention": ["Regular care"]
 },
 "Tomato___Bacterial_spot": {
  "display_name": "Tomato — Bacterial spot",
  "symptoms": ["Small water-soaked spots on leaves", "Dark fruit lesions"],
  "causes": ["Bacterial infection", "Spread by water splash"],
  "remedies": ["Copper sprays", "Remove infected fruits"],
  "prevention": ["Use disease-free seed", "Avoid wet foliage"]
 },
 "Tomato___Early_blight": {
  "display_name": "Tomato — Early blight",
  "symptoms": ["Concentric brown rings on leaves", "Leaf drop"],
  "causes": ["Alternaria solani fungus", "Warm humid conditions"],
  "remedies": ["Remove affected leaves", "Fungicide applications"],
  "prevention": ["Crop rotation", "Mulch soil"]
 },
 "Tomato___Late_blight": {
  "display_name": "Tomato — Late blight",
  "symptoms": ["Water-soaked lesions", "Rapid collapse"],
  "causes": ["Phytophthora infestans", "Cool wet weather"],
  "remedies": ["Remove infected plants", "Apply fungicides"],
  "prevention": ["Avoid excess moisture", "Use resistant varieties"]
 },
 "Tomato___Leaf_Mold": {
  "display_name": "Tomato — Leaf mold",
  "symptoms": ["Yellow spots top leaf, olive mold underside", "Leaf drop"],
  "causes": ["Fungal infection", "High humidity/poor airflow"],
  "remedies": ["Remove infected leaves", "Use copper fungicides"],
  "prevention": ["Improve ventilation", "Avoid overhead watering"]
 },
 "Tomato___Septoria_leaf_spot": {
  "display_name": "Tomato — Septoria leaf spot",
  "symptoms": ["Small round leaf spots with dark border", "Premature defoliation"],
  "causes": ["Septoria fungus", "Spread by splash"],
  "remedies": ["Remove lower leaves", "Fungicide sprays"],
  "prevention": ["Mulch soil", "Crop rotation"]
 },
 "Tomato___Spider_mites Two-spotted_spider_mite": {
  "display_name": "Tomato — Spider mites",
  "symptoms": ["Tiny yellow speckles", "Fine webbing under leaves", "Leaf bronzing"],
  "causes": ["Spider mite infestation, hot/dry conditions"],
  "remedies": ["Spray water/soap solution", "Use miticide if heavy"],
  "prevention": ["Keep humidity up", "Encourage predators"]
 },
 "Tomato___Target_Spot": {
  "display_name": "Tomato — Target spot",
  "symptoms": ["Target-like leaf spots", "Leaf yellowing"],
  "causes": ["Corynespora fungus"],
  "remedies": ["Remove infected leaves", "Fungicide if needed"],
  "prevention": ["Avoid wet foliage", "Proper spacing"]
 },
 "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
  "display_name": "Tomato — TYLCV (Yellow Leaf Curl)",
  "symptoms": ["Upward leaf curling", "Stunted growth", "Yellowing"],
  "causes": ["Virus spread by whiteflies"],
  "remedies": ["Remove infected plants", "Control whiteflies"],
  "prevention": ["Use resistant varieties", "Netting/whitefly control"]
 },
 "Tomato___Tomato_mosaic_virus": {
  "display_name": "Tomato — Mosaic virus",
  "symptoms": ["Mottled light/dark leaf patterns", "Leaf distortion"],
  "causes": ["TMV virus, spread by contact/contaminated tools"],
  "remedies": ["Remove infected plants", "Sanitize tools"],
  "prevention": ["Use virus-free seed", "Avoid tobacco near plants"]
 },
 "Tomato___healthy": {
  "display_name": "Tomato — Healthy",
  "symptoms": ["No visible disease", "Green healthy foliage"],
  "causes": ["Healthy plant"],
  "remedies": ["None"],
  "prevention": ["Balanced care and monitoring"]
 }
}
