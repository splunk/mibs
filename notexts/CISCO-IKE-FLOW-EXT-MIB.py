#
# PySNMP MIB module CISCO-IKE-FLOW-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IKE-FLOW-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
cisgIpsSgTunIndex, cisgIpsSgProtocol = mibBuilder.importSymbols("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunIndex", "cisgIpsSgProtocol")
CIPsecPhase1PeerIdentityType, CIKEIsakmpDoi = mibBuilder.importSymbols("CISCO-IPSEC-TC", "CIPsecPhase1PeerIdentityType", "CIKEIsakmpDoi")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIkeFlowExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 428))
ciscoIkeFlowExtMIB.setRevisions(('2004-09-14 00:00',))
if mibBuilder.loadTexts: ciscoIkeFlowExtMIB.setLastUpdated('200409140000Z')
if mibBuilder.loadTexts: ciscoIkeFlowExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoIkeFlowExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 428, 0))
ciscoIkeFlowExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 428, 1))
ciscoIkeFlowExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 428, 2))
cifeIkeGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 1))
cifeClearAllTunnels = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("clearIPSec", 2), ("clearFCSP", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cifeClearAllTunnels.setStatus('current')
cifeTunnelExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2), )
if mibBuilder.loadTexts: cifeTunnelExtTable.setStatus('current')
cifeTunnelExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2, 1), ).setIndexNames((0, "CISCO-IKE-FLOW-EXT-MIB", "cifeTunnelExtDoi"), (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgProtocol"), (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunIndex"))
if mibBuilder.loadTexts: cifeTunnelExtEntry.setStatus('current')
cifeTunnelExtDoi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2, 1, 1), CIKEIsakmpDoi())
if mibBuilder.loadTexts: cifeTunnelExtDoi.setStatus('current')
cifeTunnelExtLocalIdenType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2, 1, 2), CIPsecPhase1PeerIdentityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifeTunnelExtLocalIdenType.setStatus('current')
cifeTunnelExtLocalIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifeTunnelExtLocalIdentity.setStatus('current')
cifeTunnelExtRemoteIdenType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2, 1, 4), CIPsecPhase1PeerIdentityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifeTunnelExtRemoteIdenType.setStatus('current')
cifeTunnelExtRemoteIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 428, 1, 2, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifeTunnelExtRemoteIdentity.setStatus('current')
cifeMIBConformances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 428, 2, 1))
cifeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 428, 2, 2))
cifeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 428, 2, 1, 1)).setObjects(("CISCO-IKE-FLOW-EXT-MIB", "cifeGlobalsGroup"), ("CISCO-IKE-FLOW-EXT-MIB", "cifeTunnelExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifeMIBCompliance = cifeMIBCompliance.setStatus('current')
cifeGlobalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 428, 2, 2, 1)).setObjects(("CISCO-IKE-FLOW-EXT-MIB", "cifeClearAllTunnels"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifeGlobalsGroup = cifeGlobalsGroup.setStatus('current')
cifeTunnelExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 428, 2, 2, 2)).setObjects(("CISCO-IKE-FLOW-EXT-MIB", "cifeTunnelExtLocalIdenType"), ("CISCO-IKE-FLOW-EXT-MIB", "cifeTunnelExtLocalIdentity"), ("CISCO-IKE-FLOW-EXT-MIB", "cifeTunnelExtRemoteIdenType"), ("CISCO-IKE-FLOW-EXT-MIB", "cifeTunnelExtRemoteIdentity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifeTunnelExtGroup = cifeTunnelExtGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IKE-FLOW-EXT-MIB", cifeTunnelExtLocalIdentity=cifeTunnelExtLocalIdentity, ciscoIkeFlowExtMIBConform=ciscoIkeFlowExtMIBConform, cifeTunnelExtRemoteIdentity=cifeTunnelExtRemoteIdentity, ciscoIkeFlowExtMIBObjects=ciscoIkeFlowExtMIBObjects, cifeMIBConformances=cifeMIBConformances, PYSNMP_MODULE_ID=ciscoIkeFlowExtMIB, cifeMIBCompliance=cifeMIBCompliance, cifeIkeGlobals=cifeIkeGlobals, cifeTunnelExtGroup=cifeTunnelExtGroup, cifeTunnelExtRemoteIdenType=cifeTunnelExtRemoteIdenType, ciscoIkeFlowExtMIBNotifs=ciscoIkeFlowExtMIBNotifs, cifeTunnelExtEntry=cifeTunnelExtEntry, cifeMIBGroups=cifeMIBGroups, ciscoIkeFlowExtMIB=ciscoIkeFlowExtMIB, cifeClearAllTunnels=cifeClearAllTunnels, cifeTunnelExtDoi=cifeTunnelExtDoi, cifeGlobalsGroup=cifeGlobalsGroup, cifeTunnelExtTable=cifeTunnelExtTable, cifeTunnelExtLocalIdenType=cifeTunnelExtLocalIdenType)
