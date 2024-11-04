#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

def createbec():
    # Input values defined
    busname = business_name.get()
    timeper = fiscal_period.get()
    clo = int(current_output.get())
    tfc = float(fixed_costs.get())
    avc = float(variable_costs.get())
    pri = float(price.get())

    # Calculates break-even point, costs and revenues at the current level of output
    beq = tfc / (pri - avc)
    bep = tfc + (avc * beq)
    cc = tfc + (avc * clo)
    cr = pri * clo

    # If the break-even point is larger than the current level of output, then the lines
    # are extrapolated a bit further from the break-even point
    if beq > clo:
        rangenums = int(((11/10) * beq) + 1)
        x = list(range(rangenums))
    # Else, the lines stop at the current level of output
    else:
        x = list(range(clo+1))

    # Calculate the two lines
    y0 = [tfc] * len(x)
    y1 = [tfc + (avc * num) for num in x]
    y2 = [pri * num for num in x]

    # Calculate the shape indicating profit or loss
    porlx = [beq, clo, clo, beq]
    porly = [bep, cc, cr, bep]

    # Clear previous plot
    for widget in plot_frame.winfo_children():
        widget.destroy()

    root.geometry('1280x800')


    # Create a new figure with dynamic size
    fig = Figure(figsize=(plot_frame.winfo_width() / 100, plot_frame.winfo_height() / 100), dpi=100)
    ax = fig.add_subplot(111)

    # Plot the two lines
    ax.plot(x, y0, label="Total Fixed Costs")
    ax.plot(x, y1, label="Total Costs")
    ax.plot(x, y2, label="Total Revenues")

    # Plot the shape indicating profit or loss
    if beq < clo:
        ax.fill(porlx, porly, "g", label="Profit")
    elif beq > clo:
        ax.fill(porlx, porly, "r", label="Loss")

    # Plot break-even point, current costs and revenues, and create annotations
    ax.scatter(beq, bep)
    if beq == clo:
        ax.annotate(f"BEQ, CLO, ({beq:.2f}, {bep:.2f})", (beq, bep))
    else:
        ax.annotate(f"BEQ, ({beq:.2f}, {bep:.2f})", (beq, bep))
        ax.scatter(clo, cc)
        ax.annotate(f"CLO (Costs), ({clo}, {cc:.2f})", (clo, cc))
        ax.scatter(clo, cr)
        ax.annotate(f"CLO (Revenues), ({clo}, {cr:.2f})", (clo, cr))
    ax.scatter(0, tfc)
    ax.annotate(f"Total fixed costs: {tfc:.2f}", (0, tfc))

    ax.set_xlabel("Quantity (Units)")
    ax.set_ylabel("Revenues/costs (USD)")
    ax.set_title(f"Break-even chart of {busname} for {timeper}")
    ax.grid(linestyle="dotted")
    ax.axvspan(beq, clo, facecolor="lightcyan", alpha=0.5, label="Margin of safety")
    ax.legend(loc='lower right')

    # Adjust layout to fit the figure
    fig.tight_layout()

    # Display the new plot
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Attempt to create toolbar for chart
    toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
    toolbar.update()
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH, expand=True)


# Create main window
root = tk.Tk()
root.title("BECMaker")


# Create and place input frame
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(fill=tk.X)

# Create input fields
business_name = tk.StringVar()
fiscal_period = tk.StringVar()
current_output = tk.StringVar()
fixed_costs = tk.StringVar()
variable_costs = tk.StringVar()
price = tk.StringVar()

ttk.Label(input_frame, text="Business name:").grid(row=0, column=0, sticky=tk.W)
ttk.Entry(input_frame, textvariable=business_name).grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(input_frame, text="Fiscal period:").grid(row=1, column=0, sticky=tk.W)
ttk.Entry(input_frame, textvariable=fiscal_period).grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(input_frame, text="Current level of output:").grid(row=2, column=0, sticky=tk.W)
ttk.Entry(input_frame, textvariable=current_output).grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(input_frame, text="Total fixed costs:").grid(row=3, column=0, sticky=tk.W)
ttk.Entry(input_frame, textvariable=fixed_costs).grid(row=3, column=1, sticky=(tk.W, tk.E))

ttk.Label(input_frame, text="Average variable costs:").grid(row=4, column=0, sticky=tk.W)
ttk.Entry(input_frame, textvariable=variable_costs).grid(row=4, column=1, sticky=(tk.W, tk.E))

ttk.Label(input_frame, text="Price:").grid(row=5, column=0, sticky=tk.W)
ttk.Entry(input_frame, textvariable=price).grid(row=5, column=1, sticky=(tk.W, tk.E))

# Create and place buttons
button_frame = ttk.Frame(root, padding="10")
button_frame.pack(fill=tk.X)

ttk.Button(button_frame, text="Create break-even chart", command=createbec).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Exit", command=root.quit).pack(side=tk.LEFT, padx=5)

# Create and place plot frame
plot_frame = ttk.Frame(root)
plot_frame.pack(fill=tk.BOTH, expand=True)

# Create and place toolbar frame
toolbar_frame = ttk.Frame(root)
toolbar_frame.pack(fill=tk.BOTH)

# Start the GUI event loop
root.mainloop()
