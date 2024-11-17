<div align="center">
  <h1> Product Release Naming </h1>
</div>

Traditionally, each company could have their own release protocol and naming convention. However the most common are `Major.Minor.Patch`. Within the example below we create a single branch for releases with the name format being `Release-Year-nᵗʰ release`, where the pointy/patchs are tags within the branch. For example, the branch `Release.2020.2` would be made for a release, meaning it will be sent to a customer. Further fixes would be done on the branch, however another branch would not be made. The fixes would be committed on that branch and when a another release is to be made, it would be tagged with an addition number, this number is typically referred to as a patch or point, e.g. `Release-2020.2.1`.

![](./images/releases.png)

# General Rules

Generally, `X.Y.X` is used and corresponds to `major.minor.patch`

#### Major

Major version numbers change whenever there is some significant change being introduced. For example, a large or potentially backward-incompatible change to a software package.

#### Minor

Minor version numbers change when a new, minor feature is introduced or when a set of smaller features is rolled out.

#### Patch

Patch numbers change when a new build of the software is released to customers. This is normally for small bug fixes. Also referred to as "pointy" bugs.

#### Other Variations

Other variations use build numbers as an additional identifier. So you may have a large number for `X.Y.Z.build` if you have many revisions that are tested between releases. I have seen a couple of packages identified by `year/month` or `year/release`. Thus a release in the month of September of 2010 might be `2010.9` or `2010.3` for the 3rd release of the year.

There are many variants to versioning. It all boils down to personal preference. Microsoft have a convention of `[major].[minor].[revision].[build]`