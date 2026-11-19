#
# PySNMP MIB module CISCO-QOS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-QOS-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoQosTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 573))
ciscoQosTcMIB.setRevisions(('2007-03-05 00:00', '2006-09-18 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQosTcMIB.setRevisionsDescriptions(('Add QosPolicerType textual convention.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoQosTcMIB.setLastUpdated('200703050000Z')
if mibBuilder.loadTexts: ciscoQosTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoQosTcMIB.setContactInfo('       Cisco Systems\n                Customer Service\n        \n        Postal: 170 W Tasman Drive\n                San Jose, CA 95134\n        \n           Tel: +1 800 553-NETS\n        \n        E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoQosTcMIB.setDescription('This module defines the textual conventions used within\n         Cisco Qos MIBs.')
class QosIpPrecedence(TextualConvention, Unsigned32):
    reference = 'RFC791 INTERNET PROTOCOL, Chapter 3.1'
    description = 'Indicates the IP precedence.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class QosQueueNumber(TextualConvention, Unsigned32):
    description = 'An integer indicates a queue number.'
    status = 'current'

class QosThresholdNumber(TextualConvention, Unsigned32):
    description = 'An integer indicates a threshold number.'
    status = 'current'

class QosMplsExpValue(TextualConvention, Unsigned32):
    description = 'An integer indicates a MPLS-EXP (experimental) value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class QosMutationMapName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form,\n        describes the name of a mutation map.'
    status = 'current'
    displayHint = '99a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 99)

class QosMutationMapNameOrEmpty(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the\n        QosMutationMapName convention. The latter defines a\n        non-empty mutation map name. This extension permits\n        the addtional value of empty string.'
    status = 'current'
    displayHint = '99a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 99)

class QosPolicerType(TextualConvention, Integer32):
    description = 'An integer indicating the type of a QoS policer.\n\n         microflow(1):     a microflow policer.\n         aggregate(2):     an aggregate policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("microflow", 1), ("aggregate", 2))

mibBuilder.exportSymbols("CISCO-QOS-TC-MIB", QosQueueNumber=QosQueueNumber, QosMplsExpValue=QosMplsExpValue, ciscoQosTcMIB=ciscoQosTcMIB, QosThresholdNumber=QosThresholdNumber, QosMutationMapNameOrEmpty=QosMutationMapNameOrEmpty, QosIpPrecedence=QosIpPrecedence, QosMutationMapName=QosMutationMapName, PYSNMP_MODULE_ID=ciscoQosTcMIB, QosPolicerType=QosPolicerType)
