package patches.buildTypes

import jetbrains.buildServer.configs.kotlin.*
import jetbrains.buildServer.configs.kotlin.ui.*

/*
This patch script was generated by TeamCity on settings change in UI.
To apply the patch, change the buildType with id = 'Build'
accordingly, and delete the patch script.
*/
changeBuildType(RelativeId("Build")) {
    params {
        add {
            password("system.refresh_token", "credentialsJSON:f1562ed9-33d4-4c7a-9427-ddcc9c23551d", label = "Refresh token", display = ParameterDisplay.HIDDEN)
        }
        add {
            password("system.access_token", "credentialsJSON:1c3c98ca-392a-40ee-87d9-a118b4fa071a", label = "Access Token", display = ParameterDisplay.HIDDEN, readOnly = true)
        }
    }
}
