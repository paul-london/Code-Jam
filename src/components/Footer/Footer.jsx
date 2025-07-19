import "./Footer.css";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer__container">
        <p className="footer__title">Park Hopper Routes</p>
        <p className="footer__paragraph">
          Your ultimate guide to exploring America's national parks through
          unforgettable road trip adventures.
        </p>
        <div className="footer__authors">
          <div className="footer__credits">
            <p className="footer__author">Paul London (DS)</p>
            <a
              href="https://github.com/paul-london"
              className="footer__author-link"
              target="_blank"
            >
              <img
                src="src\assets\git-logo.png"
                alt="GitHub logo"
                className="footer__git-logo"
              />
            </a>
          </div>
          <div className="footer__credits">
            <p className="footer__author">Priti Sagar (DS)</p>
            <a
              href="https://github.com/Priti0427"
              className="footer__author-link"
              target="_blank"
            >
              <img
                src="src\assets\git-logo.png"
                alt="GitHub logo"
                className="footer__git-logo"
              />
            </a>
          </div>
          <div className="footer__credits">
            <p className="footer__author">Thato Anderson (SWE)</p>
            <a
              href="https://github.com/Thato-A"
              className="footer__author-link"
              target="_blank"
            >
              <img
                src="src\assets\git-logo.png"
                alt="GitHub logo"
                className="footer__git-logo"
                target="_blank"
              />
            </a>
          </div>
          <div className="footer__credits">
            <p className="footer__author">Matthew Richards (SWE)</p>
            <a
              href="https://github.com/matthewrichards234"
              className="footer__author-link"
              target="_blank"
            >
              <img
                src="src\assets\git-logo.png"
                alt="GitHub logo"
                className="footer__git-logo"
              />
            </a>
          </div>
        </div>
      </div>
      <p className="footer__info">
        &copy; 2025 Park Hopper Routes. All rights reserved. | Privacy Policy |
        Terms of Service
      </p>
    </footer>
  );
}

export default Footer;
