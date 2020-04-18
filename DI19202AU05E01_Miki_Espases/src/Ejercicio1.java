import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;

import javax.swing.JFrame;
import javax.swing.JTextPane;

import net.sf.jasperreports.engine.JRException;

import java.awt.Color;
import javax.swing.JLabel;
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.JCheckBox;

public class Ejercicio1 extends JFrame {
	private JTextField textField;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Ejercicio1 frame = new Ejercicio1();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Ejercicio1() {
		try {
			BDQuery bd = new BDQuery();
			ArrayList<String> dept = bd.getDepartamentos();
			Object[] departamentos = dept.toArray();

			setBounds(100, 100, 450, 300);
			setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			getContentPane().setLayout(null);

			JLabel lblInforme = new JLabel("Informe 1");
			lblInforme.setBounds(10, 11, 77, 27);
			getContentPane().add(lblInforme);

			JLabel lblDepartamento = new JLabel("Departamento:");
			lblDepartamento.setBounds(79, 100, 89, 14);
			getContentPane().add(lblDepartamento);

			JComboBox comboBox = new JComboBox();
			DefaultComboBoxModel dm = new DefaultComboBoxModel(departamentos);
			comboBox.setModel(dm);

			comboBox.setBounds(169, 97, 138, 20);
			getContentPane().add(comboBox);



			JLabel lblGuardarComo = new JLabel("Guardar como:");
			lblGuardarComo.setBounds(79, 128, 77, 14);
			getContentPane().add(lblGuardarComo);

			textField = new JTextField();
			textField.setBounds(169, 125, 138, 20);
			getContentPane().add(textField);
			textField.setColumns(10);
			
			JCheckBox chckbxHtml = new JCheckBox("HTML");
			chckbxHtml.setBounds(10, 149, 97, 23);
			getContentPane().add(chckbxHtml);
			
			JCheckBox chckbxCsv = new JCheckBox("CSV");
			chckbxCsv.setBounds(10, 169, 97, 23);
			getContentPane().add(chckbxCsv);

			JButton btnVer = new JButton("Guardar");
			btnVer.addActionListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					String guardar = textField.getText().toString();
					try {
						PDF pdf = new PDF("Ej1", guardar, comboBox.getSelectedItem().toString());
						
						if (chckbxHtml.isSelected()) {
							pdf.exportHTML("Ej1", guardar, comboBox.getSelectedItem().toString());
						}
						
						if (chckbxCsv.isSelected()) {
							pdf.exportCSV("Ej1", guardar, comboBox.getSelectedItem().toString());
						}
						
					} catch (ClassNotFoundException | JRException | SQLException e1) {
						e1.printStackTrace();
					}
				}
			});
			btnVer.setBounds(141, 180, 131, 35);
			getContentPane().add(btnVer);
				
		} catch (ClassNotFoundException | SQLException e2) {
			e2.printStackTrace();
		}

	}
}
