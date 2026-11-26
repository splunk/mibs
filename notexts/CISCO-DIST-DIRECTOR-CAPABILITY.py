#
# PySNMP MIB module CISCO-DIST-DIRECTOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DIST-DIRECTOR-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
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
ciscoDistDirCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 267))
ciscoDistDirCapability.setRevisions(('2002-04-23 00:00',))
if mibBuilder.loadTexts: ciscoDistDirCapability.setLastUpdated('200204230000Z')
if mibBuilder.loadTexts: ciscoDistDirCapability.setOrganization('Cisco Systems, Inc.')
ciscoDistDirCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 267, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDistDirCapabilityV12R02 = ciscoDistDirCapabilityV12R02.setProductRelease('Cisco IOS 12.2(8)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDistDirCapabilityV12R02 = ciscoDistDirCapabilityV12R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-DIST-DIRECTOR-CAPABILITY", ciscoDistDirCapability=ciscoDistDirCapability, ciscoDistDirCapabilityV12R02=ciscoDistDirCapabilityV12R02, PYSNMP_MODULE_ID=ciscoDistDirCapability)
