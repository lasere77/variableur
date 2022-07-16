path = "index.java"

file = open(path, "w", encoding="UTF-8")

cells_nomber = 800

base1 = """
package fr.lasere.cancer_simulator.Circle;

import java.util.Random;

import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;

public class CustomCircle {

	double width = 1025;
	double height = 650;
	
	Random rand = new Random();
	
	public Circle propertyCell(Circle cell, double X, double Y) {
		int random = rand.nextInt((15 - 7) + 7) + 7;
		cell.setCenterX(X + random);
		cell.setCenterY(Y + random);
		cell.setRadius(5);
		cell.setFill(Color.LIME);
		return cell;
	} 
	
	public Circle[] init() {
"""
def cells():
    file.write(base1)
    l1 = 0
    l2 = 0
    l3 = 0
    l4 = 0
    l5 = 0
    l6 = 0
    l7 = 0
    l8 = 0
    l9 = 0
    l10 = 0
    l11 = 0
    l12 = 0
    l13 = 0
    l14 = 0
    l15 = 0
    l16 = 0
    l17 = 0
    l18 = 0
    l19 = 0
    for i in range(cells_nomber):
        if i >= 1099 and i < 10949:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l19}, height-475);\n\n"
            l19 += 20
            file.write(result)
        if i >= 949 and i < 1099:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l18}, height-450);\n\n"
            l18 += 20
            file.write(result)
        if i >= 899 and i < 949:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l17}, height-425);\n\n"
            l17 += 20
            file.write(result)
        if i >= 849 and i < 899:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l16}, height-400);\n\n"
            l16 += 20
            file.write(result)
        if i >= 799 and i < 849:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l15}, height-375);\n\n"
            l15 += 20
            file.write(result)
        if i >= 749 and i < 799:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l14}, height-325);\n\n"
            l14 += 20
            file.write(result)
        if i >= 699 and i < 749:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l13}, height-300);\n\n"
            l13 += 20
            file.write(result)
        if i >= 649 and i < 699:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l12}, height-275);\n\n"
            l12 += 20
            file.write(result)
        if i >= 599 and i < 649:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l11}, height-250);\n\n"
            l11 += 20
            file.write(result)
        if i >= 449 and i < 599:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l10}, height-225);\n\n"
            l10 += 20
            file.write(result)
        if i >= 399 and i < 449:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l9}, height-200);\n\n"
            l9 += 20
            file.write(result)
        if i >= 349 and i < 399 :
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l8}, height-175);\n\n"
            l8 += 20
            file.write(result)
        if i >= 299 and i < 349 :
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l7}, height-150);\n\n"
            l7 += 20
            file.write(result)
        if i >= 249 and i < 299 :
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l6}, height-125);\n\n"
            l6 += 20
            file.write(result)
        if i >= 199 and i < 249:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l5}, height-100);\n\n"
            l5 += 20
            file.write(result)
        if i >= 149 and i < 199:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l4}, height-75);\n\n"
            l4 += 20
            file.write(result)
        if i >= 99 and i < 149:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l3}, height-50);\n\n"
            l3 += 20
            file.write(result)
        if i >= 50 and i < 99:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l2}, height-25);\n\n"
            l2 += 20
            file.write(result)
        if i <= 49:
            result = f"        Circle cell{i} = new Circle();\n" \
                     f"        cell{i} = propertyCell(cell{i}, width-{l1}, height);\n\n"
            l1 += 20
            file.write(result)
    file.write(base2)

base2 = """
		Circle[] all_cells = {
"""
def set_list():
    for i in range(cells_nomber):
        res = f"cell{i}, "
        file.write(res)
    file.write(base3)
base3 = """
		};
		return all_cells;
	}
}
"""

cells()
set_list()
