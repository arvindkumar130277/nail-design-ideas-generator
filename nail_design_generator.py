import json

# Sample nail design ideas data
nail_designs_data = {
    "wedding": [
        "Elegant French tips with a touch of gold glitter.",
        "Soft pastel ombre with floral designs.",
        "Classic white with silver rhinestones for a glamorous look.",
        "Nude nails with delicate lace designs and pearls.",
        "All-white with a minimalistic touch of glitter and gemstones."
    ],
    "birthday": [
        "Bright neon colors with fun geometric patterns.",
        "Shimmering metallic nails with confetti accents.",
        "Bold red with black abstract lines for a chic look.",
        "Pink and purple gradient with rhinestones.",
        "Cute cupcake designs with pastel colors."
    ],
    "party": [
        "Glossy black nails with silver glitter tips.",
        "Bright colored nails with a holographic top coat.",
        "Glitter ombre nails in a mix of pink, gold, and silver.",
        "Colorful stripes with matte finishes for a trendy look.",
        "All gold nails with shimmering chrome effect."
    ],
    "casual": [
        "Simple nude nails with a glossy finish.",
        "Soft pink with minimalist gold accents.",
        "Clear coat with tiny white dots for a fresh and simple look.",
        "Muted lavender with a matte top coat.",
        "Soft beige with a small white geometric design on one nail."
    ],
    "holiday": [
        "Red and green nails with Christmas tree designs.",
        "Sparkling gold and silver for a New Year’s Eve look.",
        "Snowflake designs with a blue and white color palette for winter.",
        "Pumpkin orange and black for Halloween with spooky designs.",
        "Festive red and white striped nails for a Christmas vibe."
    ]
}

# Function to get user input for the occasion and preferences
def get_user_input():
    print("Welcome to the Nail Design Ideas Generator!")
    occasion = input("Enter the occasion (e.g., wedding, birthday, party, casual, holiday): ").strip().lower()
    nail_shape = input("Enter your preferred nail shape (e.g., oval, square, stiletto, almond): ").strip()
    color_preference = input("Enter your color preference (optional): ").strip()
    
    return {
        "occasion": occasion,
        "nail_shape": nail_shape,
        "color_preference": color_preference
    }

# Function to generate nail design ideas based on user input
def generate_nail_designs(user_profile):
    occasion = user_profile['occasion']
    nail_shape = user_profile['nail_shape']
    color_preference = user_profile['color_preference']

    # Fetch the nail designs for the selected occasion
    designs = nail_designs_data.get(occasion, [])

    # Filter the designs based on the color preference, if provided
    if color_preference:
        designs = [design for design in designs if color_preference.lower() in design.lower()]
    
    # Add a note about the nail shape to the designs
    designs = [f"{design} (Suggested for {nail_shape} shape)" for design in designs]
    
    return designs

# Function to save the selected nail designs to a text file
def save_nail_designs(designs, occasion):
    file_name = f"nail_designs_for_{occasion}.txt"
    with open(file_name, "w") as file:
        for design in designs:
            file.write(f"{design}\n")
    print(f"Your nail design ideas have been saved to {file_name}!")

# Main function to run the tool
def main():
    user_profile = get_user_input()
    nail_design_ideas = generate_nail_designs(user_profile)
    
    if nail_design_ideas:
        print("\nHere are some nail design ideas for your occasion:")
        print("-" * 50)
        for idea in nail_design_ideas:
            print(f"- {idea}")
        print("-" * 50)
        
        save_choice = input("\nWould you like to save these nail designs to a file? (yes/no): ").strip().lower()
        if save_choice == "yes":
            save_nail_designs(nail_design_ideas, user_profile['occasion'])
    else:
        print("\nSorry, we couldn't find any nail designs matching your preferences.")

if __name__ == "__main__":
    main()
