#
# PySNMP MIB module CISCO-LWAPP-DOT11-CLIENT-CALIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LWAPP-DOT11-CLIENT-CALIB-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappDot11ClientCalibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 502))
ciscoLwappDot11ClientCalibCapability.setRevisions(('2006-05-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setRevisionsDescriptions(('Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setLastUpdated('200605160000Z')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setContactInfo('             Cisco Systems\n                              Customer Service\n\n                      Postal: 170 W Tasman Drive\n                              San Jose, CA  95134\n                              USA\n  \n                         Tel: +1 800 553-NETS\n \n                      E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setDescription('Agent capabilities for \n                 CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB. ')
ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 502, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0 = ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0 = ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0.setDescription('CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB\n                         capabilities. ')
mibBuilder.exportSymbols("CISCO-LWAPP-DOT11-CLIENT-CALIB-CAPABILITY", PYSNMP_MODULE_ID=ciscoLwappDot11ClientCalibCapability, ciscoLwappDot11ClientCalibCapability=ciscoLwappDot11ClientCalibCapability, ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0=ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0)
