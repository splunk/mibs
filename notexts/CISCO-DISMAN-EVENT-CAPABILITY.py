#
# PySNMP MIB module CISCO-DISMAN-EVENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DISMAN-EVENT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cdismanEventCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 473))
cdismanEventCapability.setRevisions(('2006-01-16 00:00',))
if mibBuilder.loadTexts: cdismanEventCapability.setLastUpdated('200601160000Z')
if mibBuilder.loadTexts: cdismanEventCapability.setOrganization('Cisco Systems, Inc.')
cdismanEventCapabilityIOSXRV3R2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 473, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdismanEventCapabilityIOSXRV3R2R0CRS1 = cdismanEventCapabilityIOSXRV3R2R0CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdismanEventCapabilityIOSXRV3R2R0CRS1 = cdismanEventCapabilityIOSXRV3R2R0CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-DISMAN-EVENT-CAPABILITY", cdismanEventCapabilityIOSXRV3R2R0CRS1=cdismanEventCapabilityIOSXRV3R2R0CRS1, cdismanEventCapability=cdismanEventCapability, PYSNMP_MODULE_ID=cdismanEventCapability)
