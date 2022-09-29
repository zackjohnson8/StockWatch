import jetbrains.buildServer.configs.kotlin.*
import jetbrains.buildServer.configs.kotlin.buildSteps.python
import jetbrains.buildServer.configs.kotlin.triggers.vcs

/*
The settings script is an entry point for defining a TeamCity
project hierarchy. The script should contain a single call to the
project() function with a Project instance or an init function as
an argument.

VcsRoots, BuildTypes, Templates, and subprojects can be
registered inside the project using the vcsRoot(), buildType(),
template(), and subProject() methods respectively.

To debug settings scripts in command-line, run the

    mvnDebug org.jetbrains.teamcity:teamcity-configs-maven-plugin:generate

command and attach your debugger to the port 8000.

To debug in IntelliJ Idea, open the 'Maven Projects' tool window (View
-> Tool Windows -> Maven Projects), find the generate task node
(Plugins -> teamcity-configs -> teamcity-configs:generate), the
'Debug' option is available in the context menu for the task.
*/

version = "2022.04"

project {

    buildType(Build)
}

object Build : BuildType({
    name = "Build"
    params{
        password("refresh_token", "credentialsJSON:f1562ed9-33d4-4c7a-9427-ddcc9c23551d")
        password("client_id", "credentialsJSON:6a559562-d646-49b6-beef-a8ba26f95623")
        password("redirect_url", "credentialsJSON:80cf627a-4fc5-45b5-8d32-c4e4def55f0d")
    }

    vcs {
        root(DslContext.settingsRoot)
    }

    steps {
        python {
            environment = venv {
                requirementsFile = "requirements.txt"
            }
            command = file {
                filename = "main.py"
                scriptArguments = "-r %refresh_token% -c %client_id% -u %redirect_url%"
            }
        }
        python {
            environment = venv {
                requirementsFile = "requirements.txt"
            }
            name = "Tests"
            command = pytest {
            }
        }
    }

    triggers {
        vcs {
        }
    }
})
