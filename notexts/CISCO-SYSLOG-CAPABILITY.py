#
# PySNMP MIB module CISCO-SYSLOG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SYSLOG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSyslogCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 61))
ciscoSyslogCapability.setRevisions(('2010-01-22 14:32', '2008-08-11 00:00', '2008-06-08 00:00', '2006-10-26 00:00', '2006-05-25 00:00', '2004-02-03 00:00',))
if mibBuilder.loadTexts: ciscoSyslogCapability.setLastUpdated('201001221432Z')
if mibBuilder.loadTexts: ciscoSyslogCapability.setOrganization('Cisco Systems, Inc.')
ciscoSyslogCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCatOSV08R0101 = ciscoSyslogCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCatOSV08R0101 = ciscoSyslogCapCatOSV08R0101.setStatus('current')
ciscoSyslogCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapACSWV03R000 = ciscoSyslogCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n \n                   for Application Control Engine(ACE)\n\n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapACSWV03R000 = ciscoSyslogCapACSWV03R000.setStatus('current')
ciscoSyslogCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTSV100 = ciscoSyslogCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTSV100 = ciscoSyslogCapCTSV100.setStatus('current')
ciscoSyslogCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTMV1000 = ciscoSyslogCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTMV1000 = ciscoSyslogCapCTMV1000.setStatus('current')
ciscoSyslogCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapc4710aceVA1R70 = ciscoSyslogCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapc4710aceVA1R70 = ciscoSyslogCapc4710aceVA1R70.setStatus('current')
ciscoSyslogCapVqe = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapVqe = ciscoSyslogCapVqe.setProductRelease('VQE 3.5 release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapVqe = ciscoSyslogCapVqe.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSLOG-CAPABILITY", ciscoSyslogCapCTMV1000=ciscoSyslogCapCTMV1000, ciscoSyslogCapVqe=ciscoSyslogCapVqe, PYSNMP_MODULE_ID=ciscoSyslogCapability, ciscoSyslogCapCTSV100=ciscoSyslogCapCTSV100, ciscoSyslogCapACSWV03R000=ciscoSyslogCapACSWV03R000, ciscoSyslogCapCatOSV08R0101=ciscoSyslogCapCatOSV08R0101, ciscoSyslogCapc4710aceVA1R70=ciscoSyslogCapc4710aceVA1R70, ciscoSyslogCapability=ciscoSyslogCapability)
