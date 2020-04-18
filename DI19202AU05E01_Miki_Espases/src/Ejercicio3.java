import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import net.sf.jasperreports.engine.JRException;

import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JTextField;

public class Ejercicio3 extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	private JTextField textField_1;
	private JTextField textField_2;
	private JTextField textField_3;
	private JTextField textField_4;
	private JTextField textField_5;
	private JTextField textField_6;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Ejercicio3 frame = new Ejercicio3();
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
	public Ejercicio3() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 489, 323);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblInforme = new JLabel("Informe 3");
		lblInforme.setBounds(10, 11, 66, 14);
		contentPane.add(lblInforme);
		
		JLabel lblFechaInicio = new JLabel("Fecha inicio:");
		lblFechaInicio.setBounds(72, 71, 84, 14);
		contentPane.add(lblFechaInicio);
		
		JLabel lblFechaFinal = new JLabel("Fecha final:");
		lblFechaFinal.setBounds(71, 96, 66, 14);
		contentPane.add(lblFechaFinal);
		
		JLabel lblDia = new JLabel("dia");
		lblDia.setBounds(147, 71, 25, 14);
		contentPane.add(lblDia);
		
		JLabel lblMes = new JLabel("mes");
		lblMes.setBounds(188, 71, 31, 14);
		contentPane.add(lblMes);
		
		JLabel lblAo = new JLabel("a\u00F1o");
		lblAo.setBounds(236, 71, 34, 14);
		contentPane.add(lblAo);
		
		textField = new JTextField();
		textField.setBounds(166, 68, 19, 20);
		contentPane.add(textField);
		textField.setColumns(10);
		
		textField_1 = new JTextField();
		textField_1.setBounds(217, 68, 19, 20);
		contentPane.add(textField_1);
		textField_1.setColumns(10);
		
		textField_2 = new JTextField();
		textField_2.setColumns(10);
		textField_2.setBounds(258, 68, 38, 20);
		contentPane.add(textField_2);
		
		JLabel label = new JLabel("dia");
		label.setBounds(147, 96, 25, 14);
		contentPane.add(label);
		
		JLabel label_1 = new JLabel("mes");
		label_1.setBounds(186, 96, 30, 14);
		contentPane.add(label_1);
		
		JLabel label_2 = new JLabel("a\u00F1o");
		label_2.setBounds(236, 96, 41, 14);
		contentPane.add(label_2);
		
		textField_3 = new JTextField();
		textField_3.setColumns(10);
		textField_3.setBounds(166, 93, 19, 20);
		contentPane.add(textField_3);
		
		textField_4 = new JTextField();
		textField_4.setColumns(10);
		textField_4.setBounds(217, 93, 19, 20);
		contentPane.add(textField_4);
		
		textField_5 = new JTextField();
		textField_5.setColumns(10);
		textField_5.setBounds(258, 93, 38, 20);
		contentPane.add(textField_5);
		
		JCheckBox chckbxHtml = new JCheckBox("HTML");
		chckbxHtml.setBounds(10, 149, 97, 23);
		getContentPane().add(chckbxHtml);
		
		JCheckBox chckbxCsv = new JCheckBox("CSV");
		chckbxCsv.setBounds(10, 169, 97, 23);
		getContentPane().add(chckbxCsv);
		
		JLabel lblGuardarComo = new JLabel("Guardar como");
		lblGuardarComo.setBounds(72, 130, 66, 14);
		contentPane.add(lblGuardarComo);
		
		textField_6 = new JTextField();
		textField_6.setBounds(147, 127, 118, 20);
		contentPane.add(textField_6);
		textField_6.setColumns(10);
		
		JButton btnGuardar = new JButton("Guardar");
		btnGuardar.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				String diaInicio = textField.getText().toString();
				String mesInicio = textField_1.getText().toString();
				String anoInicio = textField_2.getText().toString();
				String diaFin = textField_3.getText().toString();
				String mesFin = textField_4.getText().toString();
				String anoFin = textField_5.getText().toString();
				String guardar = textField_6.getText().toString();
				
				try {
					PDF pdf = new PDF("Ej3", guardar, "0");
					
					int n = 0;
					
					pdf.setFechaInicio(diaInicio, mesInicio, anoInicio);
					pdf.setFechaFinal(diaFin, mesFin, anoFin);
					
					if (chckbxHtml.isSelected() && chckbxCsv.isSelected()) {
						n = 3;
						
					} else if (chckbxHtml.isSelected()) {
						n = 1;
						
					} else if (chckbxCsv.isSelected()) {
						n = 2;
						
					}
					
					pdf.ej3(guardar, n);

				} catch (ClassNotFoundException | JRException | SQLException e1) {
					e1.printStackTrace();
				}
			}
		});
		
		btnGuardar.setBounds(188, 169, 108, 46);
		contentPane.add(btnGuardar);
	}
}
