# JFLAP_Tester_python

I created this repository to automate testing for the Finite Automata assignments from the *Theoretical Foundations of Computing* course.  
This tool loads `.jff` files generated with JFLAP, runs input strings through each automaton, and checks whether the output matches the expected acceptance or rejection.  
It is intended to help students and instructors validate finite automata implementations quickly and consistently.

The project is written in Python and integrates with external Java libraries for XML parsing and JFLAP simulation.

## 📦 Requirements

Before running the project, you need to create a `libs` folder in the root of the project and add the following JAR files:

- **Xerces** (for XML file parsing): [xercesImpl-2.12.2.jar](https://mvnrepository.com/artifact/xerces/xercesImpl/2.12.2)
- **JFLAP CLI Library** (for automaton execution): [jflaplib-cli.jar](https://github.com/citiususc/jflap-lib/releases)

## ▶️ How to Run

Once the required JARs are added to the `libs` folder, run the project with the following command:

```bash
python jflap_tester.py /path/to/your/automata_directory
```

The provided directory must contain the following structure:

```
/your_directory/
│
├── automatos/
│   ├── 1.jff
│   ├── 2.jff
│   └── ...
│
├── entradas/
│   ├── 1.txt
│   ├── 2.txt
│   └── ...
│
└── saidas/
    ├── 1.txt
    ├── 2.txt
    └── ...
```

- Each file in `automatos/` is a `.jff` file representing a finite automaton (e.g., `1.jff`, `2.jff`, ...).
- Each corresponding file in `entradas/` contains a list of input strings (one per line) to be tested against the automaton.
- Each file in `saidas/` must contain `true` or `false` values indicating whether the respective input string is accepted or rejected.

## 💡 Example

Given:
- `automatos/1.jff`
- `entradas/1.txt`:
  ```
  aa
  ab
  ba
  ```
- `saidas/1.txt`:
  ```
  true
  false
  true
  ```

The script will run `aa`, `ab`, and `ba` through `1.jff` and compare the actual results with the expected values in `saidas/1.txt`.

## 🧑‍💻 Author

Developed by [Atos Brito Omena].
