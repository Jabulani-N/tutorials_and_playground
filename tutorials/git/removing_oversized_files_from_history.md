## Large File Removal

If you accidentally attempt to push a file larger than 100Mb to Git, causing `Large files detected` becuase `this exceeds GitHub's file size limit of 100.00 MB`:

**if you have not made any more commits** yet, follow [these instrucitons](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

**If you have made other commits** since the oversized file commit, you'll use [BFG Repo Cleaner](https://rtyley.github.io/bfg-repo-cleaner/).
* I was not able to have it work when following the instruciotns provided on the BFG website. To clean my repo, I instead had to put (a copy of) the executable BFG ".jar" file to the top directory of the local repository, and then do [`bfg --delete-files YOUR-FILE-WITH-SENSITIVE-DATA`](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
  * replace `bfg` with whatever the name of the actual item has
    * for example, mine was `java -jar bfg-1.14.0.jar --delete-files NAME_OF_HUGE_FILE`
* If BFG cannot find any file and asks if the repo needs to be packed, consider [`git gc`](https://stackoverflow.com/questions/61769785/warning-no-large-blobs-matching-criteria-found-in-packfiles-does-the-repo-ne)
