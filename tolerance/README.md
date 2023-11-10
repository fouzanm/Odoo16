# Odoo Customer Tolerance Management
The Odoo Customer Tolerance Management system enhances the flexibility of sales order
processing by introducing a 'Tolerance Percentage' field for customers. This feature allows you to set
a tolerance percentage for each customer, which, upon selecting the customer in a sales order (SO),
automatically populates the tolerance percentage field on the sale order lines. The tolerance field on
the sale order line is also editable, giving you full control.
## Features
1. **Tolerance Percentage Field for Customers**: In Odoo, you can now define a 'Tolerance
Percentage' field for each customer. This field represents the acceptable variation percentage for
orders placed by the customer.
2. **Default Tolerance in Sale Order Lines**: When you select a customer in a sales order within
Odoo, the system automatically populates the tolerance percentage field on the sale order lines with
the customer's defined tolerance percentage. This streamlines the order entry process.
3. **Editable Tolerance Field in Sale Order Lines**: The tolerance field in the sale order line is
editable, allowing you to adjust the tolerance percentage if needed for a specific order or product,
providing fine-grained control.
4. **Tolerance Update in Corresponding Purchase Orders (PO) and Internal Transfers**: When
creating corresponding purchase orders and internal transfers from the sales order, the tolerance
percentage is also passed along, ensuring consistency.
5. **Tolerance Range Validation in Internal Transfers**: The system validates the quantity in the
internal transfer according to the tolerance. The quantity in the transfer should fall within the range
of (ordered quantity - tolerance) to (ordered quantity + tolerance).
6. **Warning Messages for Out-of-Tolerance Orders**: If the quantity in the internal transfer falls
below or exceeds the defined tolerance range, the system generates a warning message wizard. This
message includes options to either accept or reject the out-of-tolerance order.
## Usage
1. **Tolerance Percentage Field for Customers in Odoo**:
- In Odoo, navigate to the customer record.
- Locate the 'Tolerance Percentage' field and set the desired tolerance percentage for the
customer.
2. **Create a Sales Order in Odoo**:
- When creating a sales order within Odoo, select the customer for whom you've defined the
tolerance percentage.
3. **Default Tolerance in Sale Order Lines**:
- Upon selecting the customer in the sales order within Odoo, the tolerance percentage is
automatically populated in the sale order lines.
4. **Edit Tolerance Percentage (Optional)**:
- If necessary, you can manually edit the tolerance percentage in the sale order lines for fine-tuned
Tolerance Page 3- If necessary, you can manually edit the tolerance percentage in the sale order lines for fine-tuned
control over the order's tolerance.
5. **Tolerance Validation in Internal Transfers**:
- When creating corresponding internal transfers in Odoo from the sales order, the system
validates the quantity based on the defined tolerance.
6. **Warning Messages for Out-of-Tolerance Orders**:
- If the quantity in the internal transfer falls outside the tolerance range, a warning message wizard
will prompt you to either accept or reject the order.
With the Odoo Customer Tolerance Management system, you can efficiently manage customer-
specific tolerance percentages for orders. This solution empowers you to automate the tolerance
population in sales order lines, validate quantities in internal transfers, and handle out-of-tolerance
orders with ease, all within the Odoo environment. Streamline your order processing and ensure
customer satisfaction using this Odoo solution.