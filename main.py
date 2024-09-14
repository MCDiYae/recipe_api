from fastapi import FastAPI
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for all origins (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Sample data
categories = [
  {"id": "1", "name": "Western"},
  {"id": "2", "name": "Asian"},
  {"id": "3", "name": "Desserts"},
  {"id": "4", "name": "Italian"},
  {"id": "5", "name": "Mexican"},
  {"id": "6", "name": "Indian"},
  {"id": "7", "name": "Mediterranean"},
  {"id": "8", "name": "Middle Eastern"},
  {"id": "9", "name": "Vegetarian" },
  {"id": "10","name": "Vegan"},
  {"id": "11", "name": "Spanish"},
  # Add more categories as needed
]

recipes = [
    {
      "id": "1",
      "title": "Spaghetti Carbonara",
      "imageUrl": "https://my-app-images11.s3.amazonaws.com/spaghetti_carbonara.jpg",
      "categories": ["Italian", "trend"],
      "ingredients": [
          "Spaghetti",
          "Eggs",
          "Parmesan cheese",
          "Pancetta",
          "Black pepper"
      ],
      "steps": [
          "Cook the spaghetti.",
          "Fry the pancetta.",
          "Mix eggs and cheese.",
          "Combine spaghetti with pancetta and egg mixture.",
          "Serve with black pepper."
      ]
  },
  {
      "id": "2",
      "title": "Sushi",
      "imageUrl": "https://my-app-images11.s3.amazonaws.com/sushi.jpg",
      "categories": ["Asian","trend"],
      "ingredients": [
          "Sushi rice",
          "Nori",
          "Fish",
          "Soy sauce",
          "Wasabi"
      ],
      "steps": [
          "Cook the sushi rice.",
          "Prepare the fish.",
          "Place rice on nori.",
          "Add fish and roll.",
          "Serve with soy sauce and wasabi."
      ]
  },
  {
      "id": "3",
      "title": "Chocolate Cake",
      "imageUrl": "https://my-app-images11.s3.amazonaws.com/chocolate_cake.jpg",
      "categories": ["Desserts"],
      "ingredients": [
          "Flour",
          "Cocoa powder",
          "Sugar",
          "Eggs",
          "Butter"
      ],
      "steps": [
          "Preheat the oven.",
          "Mix dry ingredients.",
          "Add wet ingredients.",
          "Pour into a baking pan.",
          "Bake and cool."
      ]
  },
  {
      "id": "4",
      "title": "Tacos",
      "imageUrl": "https://my-app-images11.s3.amazonaws.com/tacos.jpg",
      "categories": ["Mexican"],
      "ingredients": [
          "Tortillas",
          "Ground beef",
          "Cheese",
          "Lettuce",
          "Tomatoes"
      ],
      "steps": [
          "Cook the ground beef.",
          "Prepare the toppings.",
          "Warm the tortillas.",
          "Assemble the tacos.",
          "Serve with toppings."
      ]
  },
  {
      "id": "5",
      "title": "Butter Chicken",
      "imageUrl": "https://my-app-images11.s3.amazonaws.com/butter_chicken.jpg",
      "categories": ["Indian"],
      "ingredients": [
          "Chicken",
          "Butter",
          "Tomato sauce",
          "Cream",
          "Spices"
      ],
      "steps": [
          "Marinate the chicken.",
          "Cook the chicken.",
          "Prepare the sauce.",
          "Combine chicken with sauce.",
          "Serve with rice."
      ]
  },
  {
      "id": "6",
      "title": "Greek Salad",
      "imageUrl": "https://my-app-images11.s3.amazonaws.com/greek_salad.jpg",
      "categories": ["Mediterranean"],
      "ingredients": [
          "Tomatoes",
          "Cucumbers",
          "Onions",
          "Feta cheese",
          "Olives"
      ],
      "steps": [
          "Chop the vegetables.",
          "Mix the vegetables.",
          "Add feta cheese and olives.",
          "Drizzle with olive oil.",
          "Serve chilled."
      ]
  },
  {
      "id": "7",
      "title": "Falafel",
      "imageUrl": "https://my-app-images11.s3.amazonaws.com/falafel.jpg",
      "categories": ["Middle Eastern","trend"],
      "ingredients": [
          "Chickpeas",
          "Onions",
          "Garlic",
          "Parsley",
          "Spices"
      ],
      "steps": [
          "Soak the chickpeas.",
          "Blend the ingredients.",
          "Form into balls.",
          "Fry the falafel.",
          "Serve with pita."
      ]
  },
  {
      "id": "8",
      "title": "Vegetarian Pizza",
      "imageUrl": "https://my-app-images11.s3.amazonaws.com/vegetarian_pizza.jpg",
      "categories": ["Vegetarian","trend","Italian"],
      "ingredients": [
          "Pizza dough",
          "Tomato sauce",
          "Cheese",
          "Vegetables",
          "Olive oil"
      ],
      "steps": [
          "Preheat the oven.",
          "Prepare the dough.",
          "Add sauce and toppings.",
          "Bake the pizza.",
          "Serve hot."
      ]
  },
  {
      "id": "9",
      "title": "Vegan Burger",
      "imageUrl": "https://my-app-images11.s3.amazonaws.com/vegan_burger.jpg",
      "categories": ["Vegan"],
      "ingredients": [
          "Vegan patties",
          "Buns",
          "Lettuce",
          "Tomatoes",
          "Vegan cheese"
      ],
      "steps": [
          "Cook the patties.",
          "Prepare the toppings.",
          "Assemble the burgers.",
          "Serve with sides.",
          "Enjoy."
      ]
  },
  {
      "id": "10",
      "title": "Paella",
      "imageUrl": "https://my-app-images11.s3.amazonaws.com/paella.jpg",
      "categories": ["Spanish","trend"],
      "ingredients": [
          "Rice",
          "Seafood",
          "Chicken",
          "Vegetables",
          "Spices"
      ],
      "steps": [
          "Cook the rice.",
          "Prepare the seafood and chicken.",
          "Cook the vegetables.",
          "Combine all ingredients.",
          "Serve hot."
      ]
  },
  {
    "id": "11",
    "title": "Beef Wellington",
    "imageUrl": "https://my-app-images11.s3.amazonaws.com/beef_wellington.jpg",
    "categories": ["Western"],
    "ingredients": [
        "Beef tenderloin",
        "Mushrooms",
        "Shallots",
        "Garlic",
        "Prosciutto",
        "Puff pastry",
        "Dijon mustard",
        "Egg yolk"
    ],
    "steps": [
        "Sear the beef tenderloin on all sides and let it cool.",
        "Prepare the mushroom duxelles by sautéing mushrooms, shallots, and garlic until dry.",
        "Spread Dijon mustard over the beef.",
        "Wrap the beef with prosciutto and the mushroom mixture.",
        "Encase the beef in puff pastry and brush with egg yolk.",
        "Bake at 400°F (200°C) until the pastry is golden brown."
    ]
},
{
    "id": "12",
    "title": "Chicken Pot Pie",
    "imageUrl": "https://my-app-images11.s3.amazonaws.com/chicken_pot_pie.jpg",
    "categories": ["Western"],
    "ingredients": [
        "Chicken breast",
        "Carrots",
        "Peas",
        "Potatoes",
        "Onion",
        "Butter",
        "Flour",
        "Chicken broth",
        "Milk",
        "Puff pastry"
    ],
    "steps": [
        "Cook the chicken and cut it into cubes.",
        "Sauté carrots, peas, potatoes, and onion in butter.",
        "Stir in flour to create a roux, then add chicken broth and milk to make a sauce.",
        "Mix the chicken with the sauce and vegetables.",
        "Pour the mixture into a baking dish and cover with puff pastry.",
        "Bake until the pastry is golden brown."
    ]
},
{
    "id": "13",
    "title": "Shepherd's Pie",
    "imageUrl": "https://my-app-images11.s3.amazonaws.com/shepherds_pie.jpg",
    "categories": ["Western"],
    "ingredients": [
        "Ground lamb",
        "Onions",
        "Carrots",
        "Peas",
        "Tomato paste",
        "Worcestershire sauce",
        "Beef broth",
        "Mashed potatoes",
        "Butter"
    ],
    "steps": [
        "Cook ground lamb with onions, carrots, and peas until browned.",
        "Stir in tomato paste, Worcestershire sauce, and beef broth.",
        "Simmer until thickened.",
        "Spread the meat mixture in a baking dish.",
        "Top with mashed potatoes and butter.",
        "Bake until the top is golden."
    ]
},
{
    "id": "14",
    "title": "Chicken Teriyaki",
    "imageUrl": "https://my-app-images11.s3.amazonaws.com/chicken_teriyaki.jpg",
    "categories": ["Asian","trend"],
    "ingredients": [
        "Chicken thighs",
        "Soy sauce",
        "Mirin",
        "Sugar",
        "Ginger",
        "Garlic",
        "Sesame seeds"
    ],
    "steps": [
        "Marinate the chicken in a mixture of soy sauce, mirin, sugar, ginger, and garlic.",
        "Cook the chicken in a skillet until browned.",
        "Pour the marinade over the chicken and reduce until thickened.",
        "Serve the chicken with rice.",
        "Garnish with sesame seeds and chopped green onions."
    ]
},
{
    "id": "15",
    "title": "Pad Thai",
    "imageUrl": "https://my-app-images11.s3.amazonaws.com/pad_thai.jpg",
    "categories": ["Asian"],
    "ingredients": [
        "Rice noodles",
        "Shrimp",
        "Eggs",
        "Bean sprouts",
        "Tofu",
        "Peanuts",
        "Tamarind paste",
        "Fish sauce",
        "Palm sugar",
        "Lime"
    ],
    "steps": [
        "Soak the rice noodles in warm water until soft.",
        "Stir-fry shrimp and tofu in a hot pan.",
        "Push to the side and scramble the eggs.",
        "Add noodles and mix with tamarind paste, fish sauce, and palm sugar.",
        "Toss in bean sprouts and chopped peanuts.",
        "Serve with lime wedges."
    ]
},

{
    "id": "16",
    "title": "Cheesecake",
    "imageUrl": "https://my-app-images11.s3.amazonaws.com/cheesecake.jpg",
    "categories": ["Desserts","trend"],
    "ingredients": [
        "Cream cheese",
        "Graham crackers",
        "Sugar",
        "Butter",
        "Eggs",
        "Vanilla extract",
        "Sour cream",
        "Lemon zest"
    ],
    "steps": [
        "Prepare the graham cracker crust and press it into a springform pan.",
        "Mix cream cheese, sugar, eggs, vanilla, sour cream, and lemon zest until smooth.",
        "Pour the filling over the crust.",
        "Bake in a water bath at 325°F (160°C) for 1 hour.",
        "Let it cool, then refrigerate for several hours before serving."
    ]
},
{
    "id": "17",
    "title": "Tiramisu",
    "imageUrl": "https://my-app-images11.s3.amazonaws.com/tiramisu.jpg",
    "categories": ["Desserts"],
    "ingredients": [
        "Mascarpone cheese",
        "Ladyfingers",
        "Espresso",
        "Cocoa powder",
        "Eggs",
        "Sugar",
        "Marsala wine",
        "Heavy cream"
    ],
    "steps": [
        "Whisk egg yolks and sugar until pale, then mix in mascarpone and Marsala wine.",
        "Whip the cream and fold it into the mascarpone mixture.",
        "Dip ladyfingers in espresso and layer them in a dish.",
        "Spread the mascarpone mixture over the ladyfingers.",
        "Repeat layers and chill for at least 4 hours.",
        "Dust with cocoa powder before serving."
    ]
},

]

@app.get("/categories", response_model=List[Dict])
async def get_categories():
  return categories

@app.get("/recipes", response_model=List[Dict])
async def get_recipes():
  return recipes