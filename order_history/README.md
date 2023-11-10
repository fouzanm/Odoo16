# Order History Management
The Order History Management is a comprehensive solution that enriches the customer management and sales order processes within Odoo. This enhancement introduces advanced features to streamline sales and procurement operations, improve customer insights, and enhance pricing and history management.
## Features
1. **Sale Orders Page for Customers**: Within the customer form in Odoo, a new 'Sale Orders' page is added. This page displays all sale orders associated with the corresponding customer in a tree view, providing easy access to customer-specific sales information.
2. **Smart Button for Product Count**: A smart button is included on the 'Sale Orders' page, displaying the total count of products sold to the customer. This enables quick insights into the customer's purchase history.
3. **Detailed Product View**: Clicking the smart button reveals a detailed tree view of all products that the customer has purchased, making it easy to review their buying habits.
4. **Product Sale Count Field**: Each product displayed includes a field showing the total sale count, providing information on the popularity of each item.
5. **Unit Price Synchronization**: Any changes made to the sale price of a product automatically update the unit prices in draft state sale orders, ensuring consistency.
6. **Automatic Purchase Order Creation**: Upon confirming a sale order, a purchase order is automatically created for each product, streamlining the procurement process.
7. **History Model**: A new model for saving sale order and corresponding purchase order history is introduced. This model includes fields such as `sale`, `purchase`, `partner`, `date`, `salesperson`, and `vendor`.
8. **Scheduled Action**: A scheduled action is configured to create sale order and purchase order history records for the previous day. This helps maintain a comprehensive history of transactions.
9. **Access Control**: Access to the history menu is limited to sale managers, ensuring data security and control.
## Usage
1. **Accessing Sale Orders Page for Customers in Odoo**:
-Within a customer's form in Odoo, navigate to the 'Sale Orders' page to view a tree view of all sale orders associated with that customer.
2. **Smart Button for Product Count**:
-On the 'Sale Orders' page, use the smart button to view the total count of products sold to the customer.
3. **Detailed Product View**:
-Click the smart button to access a detailed tree view of all products purchased by the customer.
4. **Product Sale Count Field**:
-Review the sale count field for each product to understand its popularity.
5. **Automatic Price Synchronization**:
-Any changes to the sale price of a product will automatically update unit prices in draft state sale orders.
6. **Purchase Order Creation**:
-Upon confirming a sale order, the system automatically generates a purchase order for each product.
7. **Sale Order and Purchase Order History**:
-Utilize the history model to access a comprehensive record of sale orders, purchase orders, and related data.
The Order History Management empowers users to efficiently manage customer relationships, sales orders, and purchase orders. With advanced features such as product insights, automatic unit price synchronization, and comprehensive transaction history, this enhancement enhances the capabilities of Odoo for sales and procurement professionals.