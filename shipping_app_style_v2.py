import tkinter as tk
import ttkbootstrap as ttkb

# Define your classes
class WeightTier:
    def __init__(self, min, max, price):
        self.min = min
        self.max = max
        self.price = price

class ShippingPlan:
    def __init__(self, company, name, weight_tiers, flat_charge):
        self.company = company
        self.name = name
        self.weight_tiers = weight_tiers
        self.flat_charge = flat_charge
        self.cost = None

    def calc_cost(self, weight):
        cost = 0
        if self.weight_tiers:
            for tier in self.weight_tiers:
                # Check if weight falls into the tier
                min_limit = tier.min
                max_limit = tier.max
                if (min_limit is None or weight > min_limit) and (max_limit is None or weight <= max_limit):
                    cost += weight * tier.price
                    break
        if self.flat_charge:
            cost += self.flat_charge
        self.cost = cost
        return cost

# Initialize your shipping plans
ground = ShippingPlan(
    company='Sergios Shipping',
    name='Ground Shipping',
    weight_tiers=[
        WeightTier(None, 2, 1.50),
        WeightTier(2, 6, 3.00),
        WeightTier(6, 10, 4.00),
        WeightTier(10, None, 4.75)
    ],
    flat_charge=20.00
)

premium = ShippingPlan(
    company='Sergios Shipping',
    name='Ground Shipping Premium',
    weight_tiers=None,
    flat_charge=125.00
)

avion_basic = ShippingPlan(
    company='Sergios Shipping',
    name='Avion Basic Shipping',
    weight_tiers=[
        WeightTier(None, 2, 4.50),
        WeightTier(2, 6, 9.00),
        WeightTier(6, 10, 12.00),
        WeightTier(10, None, 14.25)
    ],
    flat_charge=None
)

plans = [ground, premium, avion_basic]

# Create Tkinter app with ttkbootstrap
class ShippingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shipping Cost Calculator")
        style = ttkb.Style('darkly')  # Choose a theme like 'darkly', 'yeti','cosmo',etc.

        # Input frame
        input_frame = ttkb.Frame(root, padding="10")
        input_frame.grid(row=0, column=0, sticky="EW")

        ttkb.Label(input_frame, text="Enter weight (lb):").grid(row=0, column=0, sticky="W")
        self.weight_var = tk.StringVar()
        self.weight_entry = ttkb.Entry(input_frame, width=10, textvariable=self.weight_var)
        self.weight_entry.grid(row=0, column=1, padx=5)

        # Buttons frame
        button_frame = ttkb.Frame(root, padding="10")
        button_frame.grid(row=1, column=0, sticky="EW")

        self.calc_button = ttkb.Button(button_frame, text="Calculate Cheapest", command=self.calculate_cheapest)
        self.calc_button.grid(row=0, column=0, padx=5)

        self.clear_button = ttkb.Button(button_frame, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=0, column=1, padx=5)

        # Results display
        # Using tk.Text (not ttkbootstrap), since ttkbootstrap doesn't have a Text widget
        self.result_text = tk.Text(root, height=10, width=60, state='disabled', wrap='word')
        self.result_text.grid(row=2, column=0, padx=10, pady=10)

    def calculate_cheapest(self):
        # Clear previous results
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)

        try:
            weight = float(self.weight_var.get())
            if weight <= 0:
                raise ValueError
        except ValueError:
            self.result_text.insert(tk.END, "Please enter a valid positive number for weight.\n")
            self.result_text.config(state='disabled')
            return

        # Calculate costs for each plan
        for plan in plans:
            plan.calc_cost(weight)

        # Sort plans by cost
        sorted_plans = sorted(plans, key=lambda p: p.cost)
        cheapest = sorted_plans[0]

        # Display the results
        self.result_text.insert(tk.END, f"Cheapest option for weight {weight} lb:\n")
        self.result_text.insert(tk.END, f"Company: {cheapest.company}\n")
        self.result_text.insert(tk.END, f"Service: {cheapest.name}\n")
        self.result_text.insert(tk.END, f"Price: ${cheapest.cost:.2f}\n\n")
        self.result_text.insert(tk.END, "All options:\n")
        for plan in sorted_plans:
            self.result_text.insert(tk.END, f"{plan.name}: ${plan.cost:.2f}\n")
        self.result_text.config(state='disabled')

    def clear_fields(self):
        self.weight_var.set('')
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state='disabled')


# Run the app
if __name__ == "__main__":
    root = tk.Tk()

    # Set fixed window size
    root.geometry("400x400")  # Width x Height

    # Optional: disable resizing if you want to prevent user from resizing
    root.resizable(False, False)

    app = ShippingApp(root)
    root.mainloop()