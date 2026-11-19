#
# PySNMP MIB module CISCO-LWAPP-DOT11-CLIENT-CALIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LWAPP-DOT11-CLIENT-CALIB-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappDot11ClientCalibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 502))
ciscoLwappDot11ClientCalibCapability.setRevisions(('2006-05-16 00:00',))
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setLastUpdated('200605160000Z')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 502, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0 = ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0 = ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-DOT11-CLIENT-CALIB-CAPABILITY", ciscoLwappDot11ClientCalibCapability=ciscoLwappDot11ClientCalibCapability, ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0=ciscoLwappDot11ClientCalibCapabilityCUWNSV4R0, PYSNMP_MODULE_ID=ciscoLwappDot11ClientCalibCapability)
