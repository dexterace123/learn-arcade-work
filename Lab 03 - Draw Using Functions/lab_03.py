"""
This is lab_03.  My attempt to draw the starship Enterprise using functions.
"""

import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

def draw_saucer_shape(x, y):
    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    arcade.draw_circle_filled(x, y, x - 10, (229, 228, 226))
    arcade.draw_arc_outline(x, y, 100, 100, arcade.color.BLACK, 90, 270)

def draw_main_body(x, y):
    arcade.draw_lbwh_rectangle_filled(x + 170, y - 35, 300, 70, (229, 228, 226))
    arcade.draw_arc_filled(x + 470, y, 30, 70, (207, 196, 207), -90, 90)

def draw_nacelle_spokes(x, y):
    arcade.draw_lbwh_rectangle_filled(x + 360, y + 20, 30, 100, (229, 228, 226))
    arcade.draw_lbwh_rectangle_filled(x + 360, y - 120, 30, 100, (229, 228, 226))

def draw_nacelles(x, y):
    arcade.draw_lbwh_rectangle_filled(x + 260, y + 120, 480, 40, (229, 228, 226))
    arcade.draw_lbwh_rectangle_filled(x + 260, y - 160, 480, 40, (228, 228, 226))
    arcade.draw_arc_filled(x + 260, y + 140, 40, 40, arcade.color.RED, 90, 270)
    arcade.draw_arc_filled(x + 260, y - 140, 40, 40, arcade.color.RED, 90, 270)
    arcade.draw_arc_filled(x + 740, y + 140, 20, 40, (207, 196, 207), -90, 90)
    arcade.draw_arc_filled(x + 740, y - 140, 20, 40, (207, 196, 207), -90, 90)
    arcade.draw_lbwh_rectangle_filled(x + 710, y + 120, 30, 40, (207, 196, 207))
    arcade.draw_lbwh_rectangle_filled(x + 710, y - 160, 30, 40, (207, 196, 207))

def draw_saucer_details(x, y):
    arcade.draw_circle_outline(x, y, 200, arcade.color.BLACK)
    arcade.draw_circle_outline(x, y, 175, arcade.color.BLACK)
    arcade.draw_line(x, y - 50, x + 100, y, arcade.color.BLACK)
    arcade.draw_line(x, y + 50, x + 100, y, arcade.color.BLACK)
    arcade.draw_circle_outline(x, y, 20, arcade.color.BLACK)
    arcade.draw_text("U.S.S. ENTERPRISE", x - 80, y + 72, arcade.color.BLACK, 16, rotation=90)
    arcade.draw_text("N", x - 100, y + 100, arcade.color.BLACK, 30, rotation=135)
    arcade.draw_text("C", x - 125, y + 70, arcade.color.BLACK, 30, rotation=120)
    arcade.draw_text("C", x - 140, y + 35, arcade.color.BLACK, 30, rotation=105)
    arcade.draw_text("-", x - 145, y, arcade.color.BLACK, 30, rotation=90)
    arcade.draw_text("1", x - 145, y - 25, arcade.color.BLACK, 30, rotation=79)
    arcade.draw_text("7", x - 140, y - 50, arcade.color.BLACK, 30, rotation=68)
    arcade.draw_text("0", x - 130, y - 75, arcade.color.BLACK, 30, rotation=57)
    arcade.draw_text("1", x - 115, y - 100, arcade.color.BLACK, 30, rotation=45)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Starship Enterprise")
    arcade.set_background_color(arcade.color.BLACK)

    arcade.start_render()

    x_center = 210
    y_center = 300
    draw_saucer_shape(x_center, y_center)
    draw_main_body(x_center, y_center)
    draw_nacelle_spokes(x_center, y_center)
    draw_nacelles(x_center, y_center)
    draw_saucer_details(x_center, y_center)

    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()
