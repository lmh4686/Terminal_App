## Manual testing
### *Note: These tests only applied to the cases that unit test didn't cover from [test_module.py](src/test_module.py).*
### - For farms :
| Features | Case | Expected result | Test result | Pass the test
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Harvest | Item dropped bigger amount than bag's available space | Add only the amount of left over space, take user to home, transfer items to storage | As expected for all cases | O
| Skip | Appeared object is apple | Skip the current object, shows another random object | Orange appeared | O
| Check bag | Harvested 2 orange and 3 oat | Show only what are in the bag, not show other items that values are 0 | Showing 2 orange 3 oat | O
| Check recipes | N/A | Show all 4 recipes | As expected | O
| Go to Grain farm | Currently at the Fruit farm | Move to Grain farm. Grain objects to appear. | As expected, Wheat appeared | O
| Go to Fruit farm | Currently at the Grain farm | Move to Fruit farm. Fruit objects to appear. | As expected, Plum appeared | O
| Go to home | Bag has 5 orange, 3 oat, 10 corn. Storage has 3 oat | Move to home, Transfer all items to the storage | Bag gets empty, Storage has 5 orange, 6 oat, 10 corn | O
| Quit the game | N/A | Program terminated after print message | As expected | O
***
### For home : 
| Features | Case | Expected result | Test result | Pass the test
| ----------- | ----------- | ----------- | ----------- | ----------- |
| N/A | **Case A :** User just arrived home and storage has been updated to have: 12 Plum, 8 Apple, 24 Orange, 10 Wheat, 16 Oat, 8 Corn | Printed message includes a list of available dish to cook that meets the recipe with 'Choose dish to cook' option. | Message includes 1 Apple porridge 2 Plum porridge, 2 Orange porridge, 2 Mixed porridge  with 'Choose dish to cook' option. | O
| Choose dish to cook | Under same storage condition with Case A | Show a list of available dish and let user to select one | Show (1)Apple porridge, (2)Plum porridge, (3)Orange porridge, (4)Mixed porridge | O
| Cook | Under same storage condition with A, user chose Mixed porridge to cook | Ask user to type a number of dish to cook with max number guidance | "How many Mixed porridge do you want to cook? Max: 2" | O
| N/A | Continued from above, user typed 2 | Print dish with amount that user cooked, left over items after deduct 2 * items in Mixed porridge recipe from item in the storage | "You cooked 2 Mixed porridge", storage: 8 Plum, 18 Orange, 6 Wheat, 10 Oat, 6 Corn | O
| N/A | Continued from above | Show updated list of available dish to cook with 'Choose dish to cook' option | Available dish correctly updated to 1 Plum porridge and 1 Orange porridge, iterates same structure with Case A untill storage doesn't have enough item to cook | O
| N/A | Continued from above, user cook all available dish and storage doesn't have enough item to cook | Prompt users to select farms with "You don't have eonght ingredient to cook message" | As expected, both farm options worked and quit the game option worked | O
| Cook later go to farm to harvest | Continued from Case A | Prompt user to choose farm | Show (1)Go to fruit farm (2)Go to Grain farm (3)Quit the game | O
| Quit the game | Continued from Case A | Terminate the program with message | "Thank you for playing", program finished | O
| N/A | **Case B:** User just arrived home and storage has been updated to have: 3 Plum, 18 Orange, 2 Wheat, 8 Oat, 5 Corn | Prompt users to select farms with "You don't have eonght ingredient to cook message" | As expected, both farm options worked and quit the game option worked | O
***
