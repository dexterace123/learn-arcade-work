"""
This is lab_02.  My attempt to draw the starship Enterprise.
"""

import arcade

arcade.open_window(1000, 600, "Starship Enterprise")

# Set the background color
arcade.set_background_color(arcade.color.BLACK)

# Get ready to draw
arcade.start_render()

# Draw saucer
arcade.draw_circle_filled(210, 300, 200, (229, 228, 226))
arcade.draw_arc_outline(210, 300, 100, 100, arcade.color.BLACK, 90, 270)

# Draw main body
arcade.draw_lbwh_rectangle_filled(380, 265, 300, 70, (229, 228, 226))
arcade.draw_arc_filled(680, 300, 30, 70, (207, 196, 207), -90, 90)

# Draw nacelle spokes
arcade.draw_lbwh_rectangle_filled(570, 320, 30, 100, (229, 228, 226))
arcade.draw_lbwh_rectangle_filled(570, 180, 30, 100, (229, 228, 226))

# Draw nacelles
arcade.draw_lbwh_rectangle_filled(470, 420, 480, 40, (229, 228, 226))
arcade.draw_lbwh_rectangle_filled(470, 140, 480, 40, (228, 228, 226))
arcade.draw_arc_filled(470, 440, 40, 40, arcade.color.RED, 90, 270)
arcade.draw_arc_filled(470, 160, 40, 40, arcade.color.RED, 90, 270)
arcade.draw_arc_filled(950, 440, 20, 40, (207, 196, 207), -90, 90)
arcade.draw_arc_filled(950, 160, 20, 40, (207, 196, 207), -90, 90)
arcade.draw_lbwh_rectangle_filled(920, 420, 30, 40, (207, 196, 207))
arcade.draw_lbwh_rectangle_filled(920, 140, 30, 40, (207, 196, 207))

# Saucer details
arcade.draw_circle_outline(210, 300, 200, arcade.color.BLACK)
arcade.draw_circle_outline(210, 300, 175, arcade.color.BLACK)
arcade.draw_line(210, 250, 310, 300, arcade.color.BLACK)
arcade.draw_line(210, 350, 310, 300, arcade.color.BLACK)
arcade.draw_circle_outline(210, 300, 20, arcade.color.BLACK)
arcade.draw_text("U.S.S. ENTERPRISE", 130, 372, arcade.color.BLACK, 16, rotation=90)
arcade.draw_text("N", 110,400, arcade.color.BLACK, 30, rotation=135)
arcade.draw_text("C", 85,370, arcade.color.BLACK, 30, rotation=120)
arcade.draw_text("C", 70,335, arcade.color.BLACK, 30, rotation=105)
arcade.draw_text("-", 65,300, arcade.color.BLACK, 30, rotation=90)
arcade.draw_text("1", 65,275, arcade.color.BLACK, 30, rotation=79)
arcade.draw_text("7", 70,250, arcade.color.BLACK, 30, rotation=68)
arcade.draw_text("0", 80,225, arcade.color.BLACK, 30, rotation=57)
arcade.draw_text("1", 95,200, arcade.color.BLACK, 30, rotation=45)

arcade.finish_render()
arcade.run()
