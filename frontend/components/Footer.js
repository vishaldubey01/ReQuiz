import styles from "../styles/Home.module.css";

export default function Footer() {
  return (
    <footer className={styles.footer}>
      <div className="inline">
        Developed with ❤️ at
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Duke_Athletics_logo.svg/150px-Duke_Athletics_logo.svg.png"
          alt="Duke Logo"
          className={styles.logo}
          style={{ display: "inline" }}
        />{" "}
        by Vishal, Rami, and Ansh
      </div>
    </footer>
  );
}
