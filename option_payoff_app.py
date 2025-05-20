{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d07e3131",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Function to calculate individual option payoff\n",
    "def get_option_payoff(option_type, position, strike, premium, underlying_prices):\n",
    "    if option_type.lower() == \"call\":\n",
    "        payoff = np.maximum(underlying_prices - strike, 0)\n",
    "    else:  # put\n",
    "        payoff = np.maximum(strike - underlying_prices, 0)\n",
    "\n",
    "    if position.lower() == \"long\":\n",
    "        return payoff - premium\n",
    "    else:  # short\n",
    "        return -payoff + premium\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"📈 Option Strategy Payoff Calculator\")\n",
    "\n",
    "st.sidebar.header(\"Strategy Configuration\")\n",
    "\n",
    "num_options = st.sidebar.number_input(\"Number of Options\", min_value=1, max_value=10, step=1)\n",
    "\n",
    "strategy = []\n",
    "for i in range(num_options):\n",
    "    st.sidebar.subheader(f\"Option {i+1}\")\n",
    "    option_type = st.sidebar.selectbox(f\"Type (Option {i+1})\", [\"Call\", \"Put\"], key=f\"type_{i}\")\n",
    "    position = st.sidebar.selectbox(f\"Position (Option {i+1})\", [\"Long\", \"Short\"], key=f\"pos_{i}\")\n",
    "    strike = st.sidebar.number_input(f\"Strike Price (Option {i+1})\", value=100.0, key=f\"strike_{i}\")\n",
    "    premium = st.sidebar.number_input(f\"Premium (Option {i+1})\", value=0.0, key=f\"prem_{i}\")\n",
    "    strategy.append((option_type, position, strike, premium))\n",
    "\n",
    "st.sidebar.header(\"Underlying Price Range\")\n",
    "lower = st.sidebar.number_input(\"Lower Bound\", value=50.0)\n",
    "upper = st.sidebar.number_input(\"Upper Bound\", value=150.0)\n",
    "step = st.sidebar.number_input(\"Step\", value=1.0)\n",
    "\n",
    "underlying_prices = np.arange(lower, upper + step, step)\n",
    "\n",
    "# Calculate net payoff\n",
    "total_payoff = np.zeros_like(underlying_prices)\n",
    "for opt in strategy:\n",
    "    total_payoff += get_option_payoff(*opt, underlying_prices)\n",
    "\n",
    "# Plotting\n",
    "st.subheader(\"📊 Payoff Diagram\")\n",
    "fig, ax = plt.subplots()\n",
    "ax.plot(underlying_prices, total_payoff, label=\"Net Payoff\", color='blue', linewidth=2)\n",
    "ax.axhline(0, color='black', linestyle='--')\n",
    "ax.set_xlabel(\"Underlying Price at Expiry\")\n",
    "ax.set_ylabel(\"Payoff\")\n",
    "ax.set_title(\"Option Strategy Payoff\")\n",
    "ax.grid(True)\n",
    "ax.legend()\n",
    "st.pyplot(fig)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
