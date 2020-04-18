import java.io.ByteArrayOutputStream;
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import net.sf.jasperreports.engine.JRException;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.JasperReport;
import net.sf.jasperreports.engine.export.HtmlExporter;
import net.sf.jasperreports.engine.export.JRCsvExporter;
import net.sf.jasperreports.engine.export.JRPdfExporter;
import net.sf.jasperreports.export.Exporter;
import net.sf.jasperreports.export.ExporterConfiguration;
import net.sf.jasperreports.export.ExporterInput;
import net.sf.jasperreports.export.ExporterOutput;
import net.sf.jasperreports.export.OutputStreamExporterOutput;
import net.sf.jasperreports.export.SimpleCsvExporterConfiguration;
import net.sf.jasperreports.export.SimpleExporterInput;
import net.sf.jasperreports.export.SimpleHtmlExporterOutput;
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput;
import net.sf.jasperreports.export.SimplePdfExporterConfiguration;
import net.sf.jasperreports.export.SimpleWriterExporterOutput;
import net.sf.jasperreports.view.JasperViewer;

public class PDF {
	static class MySQLConnUtils {
		public static Connection getMySQLConnection()
				throws ClassNotFoundException, SQLException {
			String hostName = "127.0.0.1";
			String dbName = "employees";
			String userName = "root";
			String password = "root";
			return getMySQLConnection(hostName, dbName, userName, password);
		}

		public static Connection getMySQLConnection(String hostName, String dbName,
				String userName, String password) throws SQLException,
		ClassNotFoundException {

			// Declare the class Driver for MySQL DB
			// This is necessary with Java 5 (or older)
			// Java6 (or newer) automatically find the appropriate driver.
			// If you use Java> 5, then this line is not needed.
			Class.forName("com.mysql.cj.jdbc.Driver");

			String connectionURL = "jdbc:mysql://" + hostName + ":3306/" + dbName;

			Connection conn = DriverManager.getConnection(connectionURL, userName,
					password);
			return conn;
		}
	}
	
	ArrayList<String> inicio;
	ArrayList<String> fin;
	
	public PDF(String ejercicio, String guardar, String id) throws JRException, ClassNotFoundException, SQLException {
		if (!ejercicio.contains("Ej3")) {
			String reportSrcFile = "C:\\Users\\Miki\\JaspersoftWorkspace\\MyReports\\" + ejercicio + ".jrxml";
			
			JasperReport jasperReport = JasperCompileManager.compileReport(reportSrcFile);
			
			Connection conn = MySQLConnUtils.getMySQLConnection();

			Map parameters = new HashMap();
			
			if (ejercicio.contains("Ej1")) {
				parameters.put("dept", id);	
			} else if (ejercicio.contains("Ej2")) {
				parameters.put("emp", Integer.parseInt(id));
			} 
			
			JasperPrint print = JasperFillManager.fillReport(jasperReport,
					parameters, conn);
			
			JasperViewer jw = new JasperViewer(print, false);
			jw.setVisible(true);

			comprobarExistenciaCarpeta();
			
			exportFile(print, guardar);

			System.out.print("Done!");
		}
	}
	
	private void prepareToExportHTML(final JasperPrint print, String guardar) throws JRException {
		final Exporter exporter;

		exporter = new HtmlExporter();

		exporter.setExporterInput(new SimpleExporterInput(print));
		exporter.setExporterOutput(new SimpleHtmlExporterOutput("C:/tmp/" + guardar + ".html"));
		exporter.exportReport();
	}
	
	public void exportHTML(String ejercicio, String guardar, String id) throws ClassNotFoundException, SQLException, JRException {
		Connection conn = MySQLConnUtils.getMySQLConnection();
		Map<String, Object> parameters = new HashMap();
		
		if (ejercicio.contains("Ej1")) {
			parameters.put("dept", id);	
		} else if (ejercicio.contains("Ej2")) {
			parameters.put("emp", Integer.parseInt(id));
		} 
		
		String reportSrcFile = "C:\\Users\\Miki\\JaspersoftWorkspace\\MyReports\\" + ejercicio + ".jrxml";
		JasperReport jasperReport = JasperCompileManager.compileReport(reportSrcFile);
		
		JasperPrint print = JasperFillManager.fillReport(jasperReport, parameters, conn);
		prepareToExportHTML(print, guardar);
	}
	
	private void prepareToExportCSV(final JasperPrint print, String guardar) throws JRException {
		final Exporter exporter;
		exporter = new JRCsvExporter();
		
		exporter.setExporterInput(new SimpleExporterInput(print));
		exporter.setExporterOutput(new SimpleWriterExporterOutput(new File("C:/tmp/" + guardar + ".csv")));
		
		exporter.exportReport();
	}
	
	public void exportCSV(String ejercicio, String guardar, String id) throws ClassNotFoundException, SQLException, JRException {
		Connection conn = MySQLConnUtils.getMySQLConnection();
		Map<String, Object> parameters = new HashMap();
		
		if (ejercicio.contains("Ej1")) {
			parameters.put("dept", id);	
		} else if (ejercicio.contains("Ej2")) {
			parameters.put("emp", Integer.parseInt(id));
		} 
		
		String reportSrcFile = "C:\\Users\\Miki\\JaspersoftWorkspace\\MyReports\\" + ejercicio + ".jrxml";
		JasperReport jasperReport = JasperCompileManager.compileReport(reportSrcFile);
		
		JasperPrint print = JasperFillManager.fillReport(jasperReport, parameters, conn);
		prepareToExportCSV(print, guardar);
	}
	
	private void comprobarExistenciaCarpeta() {
		File outDir = new File("C:/tmp");
		outDir.mkdirs();
	}
	
	private void exportFile(JasperPrint print, String guardar) throws JRException {
		JRPdfExporter exporter = new JRPdfExporter();

		ExporterInput exporterInput = new SimpleExporterInput(print);
		// ExporterInput
		exporter.setExporterInput(exporterInput);

		// ExporterOutput
		OutputStreamExporterOutput exporterOutput = new SimpleOutputStreamExporterOutput(
				"C:/tmp/" + guardar + ".pdf");
		// Output
		exporter.setExporterOutput(exporterOutput);
		
		SimplePdfExporterConfiguration configuration = new SimplePdfExporterConfiguration();
		exporter.setConfiguration(configuration);
		exporter.exportReport();
	}
	
	public void ej3(String guardar, int n) throws JRException, ClassNotFoundException, SQLException {
		String reportSrcFile = "C:\\Users\\Miki\\JaspersoftWorkspace\\MyReports\\Ej3.jrxml";
		
		JasperReport jasperReport = JasperCompileManager.compileReport(reportSrcFile);
		
		Connection conn = MySQLConnUtils.getMySQLConnection();

		Map parameters = new HashMap();
		
		String fechaInicio = inicio.get(2) + "-" + inicio.get(1) + "-" + inicio.get(0);
		String fechaFin = fin.get(2) + "-" + fin.get(1) + "-" + fin.get(0);
		
		parameters.put("inicio", fechaInicio);
		parameters.put("fin", fechaFin);
		
		JasperPrint print = JasperFillManager.fillReport(jasperReport,
				parameters, conn);
		
		JasperViewer jw = new JasperViewer(print, false);
		jw.setVisible(true);

		comprobarExistenciaCarpeta();
		
		exportFile(print, guardar);

		System.out.print("Done!");
		if (n == 1) {
			prepareToExportHTML(print, guardar);
			
		} else if (n == 2) {
			prepareToExportCSV(print, guardar);
			
		} else if (n == 3) {
			prepareToExportHTML(print, guardar);
			prepareToExportCSV(print, guardar);
		}
	}
	
	public void setFechaInicio(String dia, String mes, String ano) {
		inicio = new ArrayList<String>();
		
		inicio.add(dia);
		inicio.add(mes);
		inicio.add(ano);
	}
	
	public void setFechaFinal(String dia, String mes, String ano) {
		fin = new ArrayList<String>();

		fin.add(dia);
		fin.add(mes);
		fin.add(ano);
	}
	
}
