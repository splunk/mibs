#
# PySNMP MIB module CISCO-REPORT-INTERVAL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-REPORT-INTERVAL-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoReportIntervalTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 670))
ciscoReportIntervalTcMIB.setRevisions(('2008-08-22 00:00',))
if mibBuilder.loadTexts: ciscoReportIntervalTcMIB.setLastUpdated('200808220000Z')
if mibBuilder.loadTexts: ciscoReportIntervalTcMIB.setOrganization('Cisco Systems, Inc.')
class ReportCurrentCount(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'

class ReportIntervalCount(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'

mibBuilder.exportSymbols("CISCO-REPORT-INTERVAL-TC-MIB", ciscoReportIntervalTcMIB=ciscoReportIntervalTcMIB, PYSNMP_MODULE_ID=ciscoReportIntervalTcMIB, ReportCurrentCount=ReportCurrentCount, ReportIntervalCount=ReportIntervalCount)
