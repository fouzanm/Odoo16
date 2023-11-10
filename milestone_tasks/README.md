# Milestone Project
The Milestone Project is a powerful tool designed to streamline project and task
creation based on milestones specified in sales order lines. By adding an 'Integer' field named
'Milestone' in the sale order line and implementing a 'Create Project' button, this solution empowers
Odoo users to efficiently organize tasks and projects within the Odoo environment.
## Features
1. **Milestone Field**: We introduce an 'Integer' field named 'Milestone' in the sale order line
within Odoo. This field allows you to specify a milestone for each product or service in your sales
order, seamlessly integrating with Odoo's user-friendly interface.
2. **Create Project Button**: We implement a 'Create Project' button directly within the Odoo sale
order interface. This button triggers the project creation process, providing a streamlined user
experience.
3. **Project and Task Creation**: When you click the 'Create Project' button within Odoo, the
system automatically creates a project with the sales order name and generates tasks according to
the milestone field values. Each milestone becomes a parent task, and its associated products or
services become sub-tasks, all seamlessly integrated with Odoo's project management capabilities.
4. **Example**: Let's say your Odoo sales order contains four lines, and two of these lines have a
'Milestone' field set to 1, while the other two have a 'Milestone' field set to 2. The system will create
the following structure within Odoo:
- Milestone 1 (Parent Task)
- Milestone 1 - Product Name 1 (Sub-Task)
- Milestone 1 - Product Name 2 (Sub-Task)
- Milestone 2 (Parent Task)
- Milestone 2 - Product Name 1 (Sub-Task)
- Milestone 2 - Product Name 2 (Sub-Task)

## Usage
1. **Milestone Field** within Odoo:
- In the sale order line within Odoo, locate the 'Milestone' field.
- Specify an integer value for each product or service line within Odoo to indicate the milestone.
2. **Create Project within Odoo**:
- On the sale order interface within Odoo, find the 'Create Project' button.
- Click the button to trigger the project creation process within Odoo.
3. **Project and Task Creation within Odoo**:
- After clicking 'Create Project' within Odoo, the system will:
- Create a project within Odoo with the name of the sale order.
- Generate parent tasks based on the milestone values within Odoo.
- Create sub-tasks within Odoo for each parent task, associating them with the relevant products
or services, all within the Odoo environment.
4. **Example within Odoo**:
- Follow the example mentioned above to understand how the system organizes projects and tasks
based on the milestone field within Odoo.

With the Odoo Sales Order Milestone Project Automation, you can efficiently manage projects and
tasks based on milestones defined in your sales orders, all seamlessly integrated with the Odoo
environment. This automation simplifies project organization, ensuring that each milestone is
represented as a parent task with its associated sub-tasks within Odoo. Streamline your project
management process and improve task visibility using this Odoo solution.