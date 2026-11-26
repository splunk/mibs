#
# PySNMP MIB module CISCO-SYSLOG-EVENT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SYSLOG-EVENT-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SyslogSeverity, = mibBuilder.importSymbols("CISCO-SYSLOG-MIB", "SyslogSeverity")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSyslogEventExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 270))
ciscoSyslogEventExtMIB.setRevisions(('2002-02-12 00:00',))
if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setLastUpdated('200202120000Z')
if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setOrganization('Cisco System Inc.')
ciscoSyslogEventExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 1))
cslogEventConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1))
class CslogEventDisposition(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("none", 0), ("count", 1), ("display", 2), ("notify", 3))

cslogEventDetailDefault = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noDisplay", 1), ("sparseDetail", 2), ("normalDetail", 3), ("verboseDetail", 4), ("exhaustiveDetail", 5))).clone('normalDetail')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventDetailDefault.setStatus('current')
cslogEventSeverityDispConsole = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 2), SyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventSeverityDispConsole.setStatus('current')
cslogEventSeverityDispHtmlGUI = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 3), SyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventSeverityDispHtmlGUI.setStatus('current')
cslogEventSeverityDispHtmlConsol = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 4), SyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventSeverityDispHtmlConsol.setStatus('current')
cslogEventDispositionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5), )
if mibBuilder.loadTexts: cslogEventDispositionTable.setStatus('current')
cslogEventDispositionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDispositionSeverity"))
if mibBuilder.loadTexts: cslogEventDispositionEntry.setStatus('current')
cslogEventDispositionSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 1), SyslogSeverity())
if mibBuilder.loadTexts: cslogEventDispositionSeverity.setStatus('current')
cslogEventDisposition = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 2), CslogEventDisposition().clone(namedValues=NamedValues(("none", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventDisposition.setStatus('current')
cslogEventDispositionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cslogEventDispositionCount.setStatus('current')
ciscoSlogEventExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 2))
ciscoSlogEventExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 1))
ciscoSlogEventExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2))
ciscoSlogEventExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 1, 1)).setObjects(("CISCO-SYSLOG-EVENT-EXT-MIB", "ciscoSlogEventExtConfigGroup"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "ciscoSlogEventExtStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlogEventExtCompliance = ciscoSlogEventExtCompliance.setStatus('current')
ciscoSlogEventExtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2, 1)).setObjects(("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDetailDefault"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispConsole"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispHtmlGUI"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispHtmlConsol"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDisposition"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlogEventExtConfigGroup = ciscoSlogEventExtConfigGroup.setStatus('current')
ciscoSlogEventExtStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2, 2)).setObjects(("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDispositionCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlogEventExtStatsGroup = ciscoSlogEventExtStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSLOG-EVENT-EXT-MIB", cslogEventDispositionSeverity=cslogEventDispositionSeverity, ciscoSlogEventExtMIBConformance=ciscoSlogEventExtMIBConformance, cslogEventDispositionTable=cslogEventDispositionTable, cslogEventDispositionCount=cslogEventDispositionCount, cslogEventSeverityDispConsole=cslogEventSeverityDispConsole, cslogEventConfig=cslogEventConfig, cslogEventSeverityDispHtmlConsol=cslogEventSeverityDispHtmlConsol, ciscoSlogEventExtConfigGroup=ciscoSlogEventExtConfigGroup, cslogEventSeverityDispHtmlGUI=cslogEventSeverityDispHtmlGUI, CslogEventDisposition=CslogEventDisposition, ciscoSlogEventExtMIBCompliances=ciscoSlogEventExtMIBCompliances, ciscoSlogEventExtCompliance=ciscoSlogEventExtCompliance, cslogEventDispositionEntry=cslogEventDispositionEntry, ciscoSlogEventExtMIBGroups=ciscoSlogEventExtMIBGroups, cslogEventDisposition=cslogEventDisposition, ciscoSyslogEventExtMIB=ciscoSyslogEventExtMIB, PYSNMP_MODULE_ID=ciscoSyslogEventExtMIB, ciscoSyslogEventExtMIBObjects=ciscoSyslogEventExtMIBObjects, ciscoSlogEventExtStatsGroup=ciscoSlogEventExtStatsGroup, cslogEventDetailDefault=cslogEventDetailDefault)
