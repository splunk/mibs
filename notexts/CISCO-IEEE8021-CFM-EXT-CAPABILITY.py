#
# PySNMP MIB module CISCO-IEEE8021-CFM-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IEEE8021-CFM-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Bits, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Bits", "iso", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIeee8021CfmExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 576))
ciscoIeee8021CfmExtCapability.setRevisions(('2008-12-05 00:00',))
if mibBuilder.loadTexts: ciscoIeee8021CfmExtCapability.setLastUpdated('200812050000Z')
if mibBuilder.loadTexts: ciscoIeee8021CfmExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoIeee8021CfmExtCapCatOSV08R0702 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 576, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmExtCapCatOSV08R0702 = ciscoIeee8021CfmExtCapCatOSV08R0702.setProductRelease('Cisco CatOS 8.7(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmExtCapCatOSV08R0702 = ciscoIeee8021CfmExtCapCatOSV08R0702.setStatus('current')
mibBuilder.exportSymbols("CISCO-IEEE8021-CFM-EXT-CAPABILITY", ciscoIeee8021CfmExtCapCatOSV08R0702=ciscoIeee8021CfmExtCapCatOSV08R0702, PYSNMP_MODULE_ID=ciscoIeee8021CfmExtCapability, ciscoIeee8021CfmExtCapability=ciscoIeee8021CfmExtCapability)
