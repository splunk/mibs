#
# PySNMP MIB module CISCO-IKE-CONF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IKE-CONF-CAPABILITY
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
ciscoCicIkeCfgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 489))
ciscoCicIkeCfgCapability.setRevisions(('2006-02-02 00:00',))
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setOrganization('Cisco Systems, Inc.')
cCicIkeCfgCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 489, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCicIkeCfgCapSanOSV30R1MDS9000 = cCicIkeCfgCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCicIkeCfgCapSanOSV30R1MDS9000 = cCicIkeCfgCapSanOSV30R1MDS9000.setStatus('current')
mibBuilder.exportSymbols("CISCO-IKE-CONF-CAPABILITY", ciscoCicIkeCfgCapability=ciscoCicIkeCfgCapability, PYSNMP_MODULE_ID=ciscoCicIkeCfgCapability, cCicIkeCfgCapSanOSV30R1MDS9000=cCicIkeCfgCapSanOSV30R1MDS9000)
