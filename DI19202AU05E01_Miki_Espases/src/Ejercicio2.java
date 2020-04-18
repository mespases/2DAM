import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import net.sf.jasperreports.engine.JRException;

import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JCheckBox;

public class Ejercicio2 extends JFrame {

	private JPanel contentPane;
	private JTextField textField;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Ejercicio2 frame = new Ejercicio2();
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
	public Ejercicio2() {
		try {
			BDQuery bd = new BDQuery();
			ArrayList<Integer> id = bd.getEmp_no();
			Object[] emp_no = id.toArray();
			
			
			setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			setBounds(100, 100, 450, 300);
			contentPane = new JPanel();
			contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
			setContentPane(contentPane);
			contentPane.setLayout(null);
			
			JLabel lblInforme = new JLabel("Informe 2");
			lblInforme.setBounds(10, 11, 73, 14);
			contentPane.add(lblInforme);
			
			JLabel lblTrabajador = new JLabel("Trabajador: ");
			lblTrabajador.setBounds(66, 66, 60, 14);
			contentPane.add(lblTrabajador);
			
			JComboBox comboBox = new JComboBox();
			DefaultComboBoxModel dm = new DefaultComboBoxModel(emp_no);
			comboBox.setModel(dm);
			
			comboBox.setBounds(145, 63, 134, 20);
			contentPane.add(comboBox);
			
			JLabel lblGuardarComo = new JLabel("Guardar como");
			lblGuardarComo.setBounds(66, 91, 73, 14);
			contentPane.add(lblGuardarComo);
			
			textField = new JTextField();
			textField.setBounds(145, 88, 134, 20);
			contentPane.add(textField);
			textField.setColumns(10);
			
			JCheckBox chckbxHtml = new JCheckBox("HTML");
			chckbxHtml.setBounds(10, 149, 97, 23);
			getContentPane().add(chckbxHtml);
			
			JCheckBox chckbxCsv = new JCheckBox("CSV");
			chckbxCsv.setBounds(10, 169, 97, 23);
			getContentPane().add(chckbxCsv);
			
			JButton btnGuardar = new JButton("Guardar");
			btnGuardar.addActionListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					String guardar = textField.getText().toString();
					try {
						PDF pdf = new PDF("Ej2", guardar, comboBox.getSelectedItem().toString());
						
						if (chckbxHtml.isSelected()) {
							pdf.exportHTML("Ej2", guardar, comboBox.getSelectedItem().toString());
						}
						
						if (chckbxCsv.isSelected()) {
							pdf.exportCSV("Ej2", guardar, comboBox.getSelectedItem().toString());
						}

					} catch (ClassNotFoundException | JRException | SQLException e1) {
						e1.printStackTrace();
					}
				}
			});
			
			btnGuardar.setBounds(139, 144, 121, 53);
			contentPane.add(btnGuardar);
			
		} catch (Exception e) {
			System.out.println(e);
		}
	}
}
