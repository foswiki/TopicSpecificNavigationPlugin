# ---+ DBConnectorPlugin
# This is the configuration used by the <b>ToPDFPlugin</b> and the
# <h2>Database</h2>

# **STRING**
# perl driver package
$Foswiki::cfg{Plugins}{DBConnectorPlugin}{driverPackage} = "DBD::SQLite";

# **STRING**
# DBI dsn. if you include the string %WORKINGDIR% it gets expanded to the Foswiki working directory for the plugin. This should be working/working_areas/DBConnectorPlugin
$Foswiki::cfg{Plugins}{DBConnectorPlugin}{dsn} = "dbi:SQLite:dbname=%WORKINGDIR%/foswiki.db";

# **STRING**
# primary key ( typically be a varchar(255) or similar) which is used to identify the topic 
$Foswiki::cfg{Plugins}{DBConnectorPlugin}{TableKeyField} = "topic_id";

# **BOOLEAN**
# allow calling the "createdb" rest handler. Attention, this can delete your data, so deactivate after installing!
$Foswiki::cfg{Plugins}{DBConnectorPlugin}{allowCreatedb} = 1;

# **BOOLEAN**
# path to your ttf fonts  reporsitory
$Foswiki::cfg{Plugins}{DBConnectorPlugin}{Debug} = 0;

