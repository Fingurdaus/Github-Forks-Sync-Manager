<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://github.com/LoveDoLove/github-account-repo-sync">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">GitHub Account Repo Sync</h3>

  <p align="center">
    Automate the synchronization of all forked repositories for a GitHub account with their upstream sources.
    <br />
    <a href="https://github.com/LoveDoLove/github-account-repo-sync"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LoveDoLove/github-account-repo-sync">View Demo</a>
    &middot;
    <a href="https://github.com/LoveDoLove/github-account-repo-sync/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/LoveDoLove/github-account-repo-sync/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

GitHub Account Repo Sync provides a GitHub Actions workflow to automate the process of updating all forked repositories for a specified GitHub account, ensuring they are always in sync with their upstream sources. This is useful for developers and organizations who maintain many forks and want to keep them up-to-date automatically.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [GitHub Actions](https://docs.github.com/en/actions)
- [actions/checkout](https://github.com/actions/checkout)
- [actions/setup-python](https://github.com/actions/setup-python)
- [Python](https://www.python.org/)
- [requests](https://pypi.org/project/requests/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To use this workflow in your own repository, follow the steps below.

### Prerequisites

- A GitHub repository with Actions enabled.
- A GitHub account with forked repositories you want to keep in sync.

### Installation

1. Copy the `account-repos-sync.yml` file from the `workflows/` directory into your repository's `.github/workflows/` directory.
2. Ensure your repository has access to a `GITHUB_TOKEN` secret (provided by default in GitHub Actions).
3. Commit and push the changes to your repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

- Go to the "Actions" tab in your repository.
- Select "Update Forked Repos to Upstream".
- Click "Run workflow" and enter the GitHub account username you want to update forks for.
- The workflow will:
  - Fetch all forked repositories for the specified account.
  - Attempt to update each fork to match its upstream source.

_You can also schedule this workflow or trigger it via the API as needed._

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [x] Sync all forked repositories for a GitHub account
- [ ] Add support for selective repo/branch sync
- [ ] Add scheduling and notifications
- [ ] Improve error handling and reporting

See the [open issues](https://github.com/LoveDoLove/github-account-repo-sync/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".  
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/LoveDoLove/github-account-repo-sync/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=LoveDoLove/github-account-repo-sync" alt="contrib.rocks image" />
</a>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/LoveDoLove/github-account-repo-sync](https://github.com/LoveDoLove/github-account-repo-sync)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

- [actions/checkout](https://github.com/actions/checkout)
- [actions/setup-python](https://github.com/actions/setup-python)
- [requests](https://pypi.org/project/requests/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Best README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/LoveDoLove/github-account-repo-sync.svg?style=for-the-badge
[contributors-url]: https://github.com/LoveDoLove/github-account-repo-sync/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/LoveDoLove/github-account-repo-sync.svg?style=for-the-badge
[forks-url]: https://github.com/LoveDoLove/github-account-repo-sync/network/members
[stars-shield]: https://img.shields.io/github/stars/LoveDoLove/github-account-repo-sync.svg?style=for-the-badge
[stars-url]: https://github.com/LoveDoLove/github-account-repo-sync/stargazers
[issues-shield]: https://img.shields.io/github/issues/LoveDoLove/github-account-repo-sync.svg?style=for-the-badge
[issues-url]: https://github.com/LoveDoLove/github-account-repo-sync/issues
[license-shield]: https://img.shields.io/github/license/LoveDoLove/github-account-repo-sync.svg?style=for-the-badge
[license-url]: https://github.com/LoveDoLove/github-account-repo-sync/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/logo.png
