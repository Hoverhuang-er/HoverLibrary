using System;

    namespace CalorieCounter 
    {
        class Calculation
        {
            static void Main(string[] args)
            {
                genderCheck();
                weightCheck();
                calorieCalc();
                getUserMacros();
                Console.Write("\nPress any key to close...");
                Console.ReadLine();

            public static int weight, multiplier, numCalories;

            //Gets gender of the user
            private static void genderCheck(bool onlyLetters = false)
            {
                Console.Write("Are you a male or female?\n");
                string gender = Console.ReadLine();

                for (int i = 0; i < gender.Length; i++)
                {
                    if (gender == "Male" || gender == "male" || gender == "Female" || gender == "female")
                    {
                        onlyLetters = true;
                        Console.WriteLine("You are a " + gender.ToLower() + ".\n");
                        break;
                    }
                    else
                    {
                        onlyLetters = false;
                    }
                }

                if (onlyLetters == false)
                {
                    Console.WriteLine("Please enter a valid gender.\n");
                    genderCheck();
                }
            }

            //Gets weight of the user
            private static void weightCheck()
            {

                Console.Write("Please enter your goal weight in lbs.\n");
                string lbs = Console.ReadLine();

                int.TryParse(lbs, out weight);

                Console.Write("Your goal weight is " + weight + " lbs.\n");

            }

            //Calculates macros of the user
            private static void calorieCalc()
            {
                Console.Write("\nA multiplier determines calorie intake for cutting, maintenance or bulking diets.\n");
                Console.Write("\nPlease select a calorie multiplier between 10 and 20:\n");

                string multSelect = Console.ReadLine();

                //Converts multiplier to integer
                int.TryParse(multSelect, out multiplier);

                Console.Write("Your multiplier is " + multiplier + ".\n");

                numCalories = weight * multiplier;

                Console.Write("\nYou should eat " + numCalories + " calories per day.\n");

                Console.Write("\nEnter the percentages of each macronutrient (must add up to 100%).\n");
            }

            private static void getUserMacros()
            {

                //Gets protein percentage from user
                Console.Write("Protein: ");
                string proteinNumber = Console.ReadLine();

                float proteinPercent;
                float.TryParse(proteinNumber, out proteinPercent);

                //Gets the carb percentage from user
                Console.Write("\nCarbs: ");
                string carbNumber = Console.ReadLine();

                float carbPercent;
                float.TryParse(carbNumber, out carbPercent);


                //Gets the fat percentage from user
                Console.Write("\nFat: ");
                string fatNumber = Console.ReadLine();

                float fatPercent;
                float.TryParse(fatNumber, out fatPercent);

                //Verifies user input adds up to 100%
                if (proteinPercent + carbPercent + fatPercent != 100)
                {
                    Console.Write("\nSorry! Your selected percentages must add up to 100%. Please try again.\n");
                    getUserMacros();
                }
                else
                {
                    //Calculate Protein Numbers
                    float proteinCalories = numCalories * (proteinPercent / 100);
                    float proteinGrams = proteinCalories / 4;


                    //Calculate Carb Numbers
                    float carbCalories = numCalories * (carbPercent / 100);
                    float carbGrams = carbCalories / 4;


                    //Calculate Fat Numbers
                    float fatCalories = numCalories * (fatPercent / 100);
                    float fatGrams = fatCalories / 9;


                    Console.Write("\nYour recommended macronutrient distribution:\n\n");
                    Console.Write("Protein: " + proteinCalories + " calories (" + proteinGrams.ToString("#.##") + "g)\n");
                    Console.Write("Carbs: " + carbCalories + " calories (" + carbGrams.ToString("#.##") + "g)\n");
                    Console.Write("Fat: " + fatCalories + " calories (" + fatGrams.ToString("#.##") + "g)\n");
                }
            }
        }
    }
