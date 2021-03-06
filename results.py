#! C:\Python38-32\python.exe -u

import mysql.connector as mysql
from connectlib import connect_db


def select_votes():
    """
    Retrieves all of the vote information about candidates from the Votes table
    """
    try:
        dem_votes()
        ind_votes()
        rep_votes()
    except mysql.Error as e:
        msg = "        <p>" + str(e) + "</p>"
        content.append(msg)


def dem_votes():
    """
    Finds which Democratic candidate (if any exist) has the most votes
    """
    # Prepare SELECT statements
    prep_subselect = "SELECT COUNT(*) AS Total, candidate FROM votes WHERE polParty = %s GROUP BY candidate"
    prep_select = (
        "SELECT MAX(Total), candidate FROM (" + prep_subselect + ") AS Results"
    )

    # A tuple should always be used for binding placeholders (%s)
    cursor.execute(
        prep_select, ("Democrat",)  # you use (value,) when searching for one value
    )

    results = cursor.fetchall()  # returns a list of tuples

    content.append('      <div class="content">')
    content.append("        <h3>Democrat</h3>")

    (votes, can) = results[0]  # unpacks the list of tuples

    # Checks if any results where found
    if votes != None and can != None:
        votes = "        <b>" + str(votes) + " vote(s)</b>"
        can = "        <b>" + str(can) + "</b>"
        content.append(can)
        content.append(votes)
    else:
        content.append("        <b>No votes yet!</b>")

    content.append("      </div>")


def rep_votes():
    """
    Finds which Republican candidate (if any exist) has the most votes
    """
    # Prepare SELECT statements
    prep_subselect = "SELECT COUNT(*) AS Total, candidate FROM votes WHERE polParty = %s GROUP BY candidate"
    prep_select = (
        "SELECT MAX(Total), candidate FROM (" + prep_subselect + ") AS Results"
    )

    # A tuple should always be used for binding placeholders (%s)
    cursor.execute(
        prep_select, ("Republican",)  # you use (value,) when searching for one value
    )

    results = cursor.fetchall()  # returns a list of tuples

    content.append('      <div class="content">')
    content.append("        <h3>Republican</h3>")

    (votes, can) = results[0]  # unpacks the list of tuples

    # Checks if any results where found
    if votes != None and can != None:
        votes = "        <b>" + str(votes) + " vote(s)</b>"
        can = "        <b>" + str(can) + "</b>"
        content.append(can)
        content.append(votes)
    else:
        content.append("        <b>No votes yet!</b>")

    content.append("      </div>")


def ind_votes():
    """
    Finds which Independent (Green Party and Libertarin) candidate (if any exist) has the most votes
    """
    # Prepare SELECT statements
    prep_subselect = "SELECT COUNT(*) AS Total, candidate FROM votes WHERE polParty = %s or polParty = %s GROUP BY candidate"
    prep_select = (
        "SELECT MAX(Total), candidate FROM (" + prep_subselect + ") AS Results"
    )

    # A tuple should always be used for binding placeholders (%s)
    cursor.execute(prep_select, ("Green Party", "Libertarian"))

    results = cursor.fetchall()  # returns a list of tuples

    content.append('      <div class="content">')
    content.append("        <h3>Independent</h3>")

    (votes, can) = results[0]  # unpacks the list of tuples

    # Checks if any results where found
    if votes != None and can != None:
        votes = "        <b>" + str(votes) + " vote(s)</b>"
        can = "        <b>" + str(can) + "</b>"
        content.append(can)
        content.append(votes)
    else:
        content.append("        <b>No votes yet!</b>")

    content.append("      </div>")


# Connects to the database
db = connect_db()

cursor = db.cursor(prepared=True)  # allows the prepare statement to be used

# Intializes an empty l ist of candidate information, error messages, and HTML code
content = []
select_votes()

print("Content-Type: text/html\n")

print("<!DOCTYPE html>")
print('<html lang="en">')
print("  <head>")
print("    <title>Results</title>")
print('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
print("    <!-- Font Awesome Script -->")
print("    <script")
print('      src="https://kit.fontawesome.com/855ee508c4.js"')
print('      crossorigin="anonymous"')
print("    ></script>\n")
print("    <!-- Bootstrap -->")
print("    <link")
print('      rel="stylesheet"')
print(
    '      href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"'
)
print(
    '      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"'
)
print('      crossorigin="anonymous"')
print("    />")
print(
    '    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>'
)
print(
    '    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>'
)
print(
    '    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n'
)
print("    <!-- Custom Stylesheet -->")
print('    <link rel="stylesheet" href="css/main-pages.css" />')
print("  </head>")
print("  <body>")
print("    <header>")
print("      <!-- Navbar -->")
print('      <nav class="navbar navbar-expand-sm bg-primary navbar-dark">')
print('        <div class="dropdown">')
print("          <button")
print('            class="btn btn-secondary dropdown-toggle"')
print('            type="button"')
print('            id="dropdownMenuButton"')
print('            data-toggle="dropdown"')
print('            aria-haspopup="true"')
print('            aria-expanded="false"')
print('            title="Account"')
print("          >")
print('            <i class="fas fa-user"></i> Account')
print("          </button>")
print('          <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">')
print('            <a href="account.py"')
print('            <a href="account.py" title="View Account"')
print('              ><i class="fas fa-user-edit"></i> View Account</a')
print("            >")
print('            <a href="login.html" title="Logout"')
print('              ><i class="fas fa-sign-out-alt"></i> Logout</a')
print("            >")
print("          </div>")
print("        </div>")
print('        <div class="item-container">')
print(
    '          <a href="index.html" title="Home"><i class="fas fa-home"></i> Home</a>'
)
print('          <div class="subnav">')
print(
    '            <a href="vote.html" title="Vote" class="subnav-link dropdown-toggle"'
)
print('              ><i class="fas fa-person-booth"></i> Vote')
print("            </a>")
print('            <div class="subnav-content">')
print('              <a href="results.py" title="Results"')
print('                ><i class="fas fa-poll"></i> Results</a')
print("              >")
print("            </div>")
print("          </div>")
print('          <a href="donation.html" title="Donation"')
print('            ><i class="fas fa-hand-holding-usd"></i> Donation</a')
print("          >")
print("        </div>")
print("      </nav>")
print("    </header>")
print('    <div id="main">')
print('      <h1 id="heading">Results</h1>')


# Prints all of the content in the list
for i in range(len(content)):
    print(content[i])

print("    </div>")
print("    <footer>")
print("    </footer>")
print("  </body>")
print("</html>")