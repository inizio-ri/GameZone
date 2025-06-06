from graphviz import Digraph

# Create a UML class diagram using Graphviz
uml_diagram = Digraph("LMS_UML_Diagram", format="png")

# Define the classes with their attributes and methods
uml_diagram.node(
    "User",
    """
    User
    -------------------
    + userId: string
    + name: string
    + email: string
    + role: string
    -------------------
    + register()
    + login()
    + enrollCourse()
    + viewContent()
    """,
    shape="record",
    style="rounded,filled",
    fillcolor="#a3c9f1"
)

uml_diagram.node(
    "Frontend",
    """
    Frontend (UI)
    -------------------
    + handleInput()
    + validateForm()
    + displayData()
    """,
    shape="record",
    style="rounded,filled",
    fillcolor="#a3f1d3"
)

uml_diagram.node(
    "Backend",
    """
    Backend Server
    -------------------
    + authenticateUser()
    + processEnrollment()
    + fetchContent()
    + manageCourses()
    """,
    shape="record",
    style="rounded,filled",
    fillcolor="#f1d6a3"
)

uml_diagram.node(
    "Database",
    """
    Database
    -------------------
    + users: Table
    + courses: Table
    + enrollments: Table
    -------------------
    + validateUser()
    + saveEnrollment()
    + retrieveContent()
    + updateCourse()
    """,
    shape="record",
    style="rounded,filled",
    fillcolor="#f1a3b0"
)

# Add relationships between the classes
uml_diagram.edge("User", "Frontend", "interacts with", arrowhead="open")
uml_diagram.edge("Frontend", "Backend", "sends requests to", arrowhead="open")
uml_diagram.edge("Backend", "Database", "queries data from", arrowhead="open")

# Save the diagram
uml_diagram_file_path = "/mnt/data/LMS_UML_Diagram.png"
uml_diagram.render(uml_diagram_file_path, cleanup=True)
uml_diagram_file_path
